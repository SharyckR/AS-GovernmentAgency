from controller.transport_factory_controller import TransportFactoryController
from controller.legal_factory_controller import LegalFactoryController
from controller.health_factory_controller import HealthFactoryController
from controller.educational_factory_controller import EducationalFactoryController
from controller.mediator import Mediator
from typing import Union
from logic.person import Person
from logic.agency_factory import AgencyFactory
from fastapi import Depends, HTTPException, status, APIRouter, Request
from fastapi.security import OAuth2PasswordRequestForm
from pymongo import MongoClient
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
from dotenv import load_dotenv
from os import getenv
from routers.send_email import send_token_authentication, is_valid_email
from logic.user_database import UserDB

load_dotenv()
mediator = Mediator()
controller_education = EducationalFactoryController()
controller_transport = TransportFactoryController()
controller_legal = LegalFactoryController()
controller_health = HealthFactoryController()
MY_CLIENT = MongoClient(getenv('MONGODB_CONNECTION_STRING'))
USERS = MY_CLIENT['USERS']
NATURAL = USERS['Natural']
LEGAL = USERS['Legal']
crypt = CryptContext(schemes=["bcrypt"])
router = APIRouter(prefix='/authentication', tags=['authentication'],
                   responses={status.HTTP_404_NOT_FOUND: {'message': 'Not found'}})


@router.post('/login')
async def login(form: OAuth2PasswordRequestForm = Depends()):
    if not (NATURAL.find_one({f'{form.username}': {"$exists": True}}) or
            LEGAL.find_one({f'{form.username}': {"$exists": True}})):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='username invalid')
    user = UserDB.search_user_db(form.username)
    if not crypt.verify(form.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='password invalid')
    access_token = {"sub": user.username,
                    "type": user.type,
                    "subtype": user.subtype,
                    "key": crypt.hash(user.username)
                    }
    if user.type == 'Legal Entity':
        access_token["exp"] = (datetime.now(timezone.utc) +
                               timedelta(weeks=float(getenv('ACCESS_TOKEN_DURATION_AGENCY'))))
    else:
        access_token["exp"] = (datetime.now(timezone.utc) +
                               timedelta(hours=float(getenv('ACCESS_TOKEN_DURATION_PERSON'))))
    await send_token_authentication(access_token=jwt.encode(access_token, getenv('SECRET'),
                                                            algorithm="HS256"),
                                    email_receiver=user.email)
    return {"access_token": jwt.encode(access_token, getenv('SECRET'), algorithm="HS256"), "token_type": "bearer"}


@router.post('/register')
async def register(user: UserDB, person: Union[Person, None] = None, agency: Union[AgencyFactory, None] = None):
    if UserDB.search_user(user.username):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='The user already exist')
    if not is_valid_email(user.email):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='The email is invalid')
    if person and int(user.username) == person.dni_person:
        mediator.add_person(person=person)
    elif agency and int(user.username) == agency.id_entity:
        if user.subtype == 'Educational Agency':
            controller_education.add_educational_agency(agency)
        elif user.subtype == 'Health Agency':
            controller_health.add_health_agency(agency)
        elif user.subtype == 'Legal Agency':
            controller_legal.add_legal_agency(agency)
        elif user.subtype == 'Transport Agency':
            controller_transport.add_transport_agency(agency)
        else:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='subtype is invalid')
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="The identifiers aren\'t equals in agency/person and user")
    user.type = user.type.title()
    user_info_dict = user.model_dump()
    user_info_dict['password'] = crypt.hash(str(user.password))
    user_info_dict = {f"{user.username}": user_info_dict}
    if user.type == 'Natural Entity':
        NATURAL.insert_one(user_info_dict)
    else:
        LEGAL.insert_one(user_info_dict)
    access_token = {"sub": user.username,
                    "type": user.type,
                    "subtype": user.subtype,
                    "key": crypt.hash(user.username)}
    if user.type == 'Legal Entity':
        access_token["exp"] = (datetime.now(timezone.utc) +
                               timedelta(weeks=float(getenv('ACCESS_TOKEN_DURATION_AGENCY'))))
    else:
        access_token["exp"] = (datetime.now(timezone.utc) +
                               timedelta(hours=float(getenv('ACCESS_TOKEN_DURATION_PERSON'))))
    await send_token_authentication(access_token=jwt.encode(access_token, getenv('SECRET'), algorithm="HS256"),
                                    email_receiver=user.email)
    return {"access_token": jwt.encode(access_token, getenv('SECRET'), algorithm="HS256"), "token_type": "bearer"}


@router.get('/verify-token', response_model=bool)
def verify_token(request: Request):
    if 'authorization' not in dict(request.headers.items()):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Missing Authorization header')
    token = dict(request.headers.items()).get('authorization').split(' ')[1]
    try:
        token_decrypted = jwt.decode(token, getenv('SECRET'), algorithms=["HS256"])
        if crypt.verify(token_decrypted.get('sub'), token_decrypted.get('key')):
            return True
    except JWTError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
    except TypeError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='The token is invalid')
    return False
