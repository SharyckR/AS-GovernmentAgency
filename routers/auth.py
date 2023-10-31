from typing import Union, Annotated, Optional
from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pymongo import MongoClient
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
from dotenv import load_dotenv
from os import getenv
from logic.legal_entity import LegalEntity
from logic.natural_entity import NaturalEntity
from middlewares.messages import send_token_authentication, is_valid_email
load_dotenv()
MY_CLIENT = MongoClient(getenv('MONGODB_CONNECTION_STRING'))
USERS = MY_CLIENT['USERS']
NATURAL = USERS['Natural']
LEGAL = USERS['Legal']
ALGORITHM = "HS256"
crypt = CryptContext(schemes=["bcrypt"])
router = APIRouter(prefix='/authentication', tags=['authentication'],
                   responses={status.HTTP_404_NOT_FOUND: {'message': 'Not found'}})
oauth2 = OAuth2PasswordBearer(tokenUrl='login')


class UserDB(LegalEntity, NaturalEntity):
    password: Optional[Union[str, int]] = "password"

    def __init__(self, **data):
        super().__init__(**data)
        if "password" not in data:
            self.password = self.username


def search_user(username: str):
    for user in NATURAL.find():
        if user.get(username):
            user_data = user.get(username)
            return NaturalEntity(**user_data)
    for user in LEGAL.find():
        if user.get(username):
            user_data = user.get(username)
            return NaturalEntity(**user_data)


def search_user_db(username: str):
    for user in NATURAL.find():
        if user.get(username):
            user_data = user.get(username)
            userdb = UserDB(**user_data)
            return userdb
    for user in LEGAL.find():
        if user.get(username):
            user_data = user.get(username)
            userdb = UserDB(**user_data)
            return userdb


async def auth_user(token: Annotated[str, Depends(oauth2)]):
    exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                              detail='Invalid authentication credentials',
                              headers={"WWW-Authenticate": "Bearer"}
                              )
    try:
        username = jwt.decode(token=token, key=getenv('SECRET'), algorithms=[ALGORITHM]).get('sub')
        if username is None:
            print('Username is None')
            raise exception
    except JWTError as e:
        print('JTW Exception ', e)
        raise exception
    return search_user(username)


async def current_user(user: Annotated[Union[NaturalEntity, LegalEntity], Depends(auth_user)]):
    if user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='The user is inactive')
    return user


@router.post('/login')
async def login(form: OAuth2PasswordRequestForm = Depends()):
    if not (NATURAL.find_one({f'{form.username}': {"$exists": True}}) or
            LEGAL.find_one({f'{form.username}': {"$exists": True}})):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='username invalid')
    user = search_user_db(form.username)
    if not crypt.verify(form.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='password invalid')
    access_token = {"sub": user.username,
                    "type": user.type,
                    "subtype": user.subtype,
                    "exp": datetime.now(timezone.utc) + timedelta(minutes=float(getenv('ACCESS_TOKEN_DURATION')))}
    await send_token_authentication(access_token=jwt.encode(access_token, getenv('SECRET'), algorithm=ALGORITHM),
                                    email_receiver=user.email)
    return {"access_token": jwt.encode(access_token, getenv('SECRET'), algorithm=ALGORITHM), "token_type": "bearer"}


@router.post('/register')
async def register(user: UserDB):
    if search_user(user.username):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='The user already exist')
    if not is_valid_email(user.email):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='The email is invalid')
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
                    "exp": datetime.now(timezone.utc) + timedelta(minutes=float(getenv('ACCESS_TOKEN_DURATION')))}
    await send_token_authentication(access_token=jwt.encode(access_token, getenv('SECRET'), algorithm=ALGORITHM),
                                    email_receiver=user.email)
    return {"access_token": jwt.encode(access_token, getenv('SECRET'), algorithm=ALGORITHM), "token_type": "bearer"}
