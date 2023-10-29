from typing import Union, Annotated, Optional
import re
from pydantic import BaseModel
from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pymongo import MongoClient
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
from dotenv import load_dotenv
from os import getenv
from middlewares.messages import send_token_authentication

load_dotenv()
MY_CLIENT = MongoClient(getenv('MONGODB_CONNECTION_STRING'))
USERS = MY_CLIENT['USERS']
USER = USERS['User']
ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 2
crypt = CryptContext(schemes=["bcrypt"])
router = APIRouter(prefix='/authentication', tags=['authentication'],
                   responses={status.HTTP_404_NOT_FOUND: {'message': 'Not found'}})
oauth2 = OAuth2PasswordBearer(tokenUrl='login')


class User(BaseModel):
    username: str
    email: str
    disabled: bool = False


class UserDB(User):
    password: Optional[Union[str, int]] = 'password'

    def __init__(self, **data):
        super().__init__(**data)
        if "password" not in data:
            self.password = self.username


def search_user(username: str):
    for user in USER.find():
        if user.get(username):
            return User(**user[username])


def search_user_db(username: str):
    for user in USER.find():
        if user.get(username):
            return UserDB(**user[username])


def is_valid_email(email):
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(email_pattern, email):
        return True
    else:
        return False


async def auth_user(token: Annotated[str, Depends(oauth2)]):
    exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                              detail='Invalid authentication credentials',
                              headers={"WWW-Authenticate": "Bearer"}
                              )
    try:
        username = jwt.decode(token=token, key=getenv('SECRET'), algorithms=[ALGORITHM]).get('sub')
        print('User: ', username)
        if username is None:
            print('Username is None')
            raise exception
    except JWTError as e:
        print('JTW Exception ', e)
        raise exception
    return search_user(username)


async def current_user(user: Annotated[User, Depends(auth_user)]):
    if user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='The user is inactive')
    return user


@router.get('/')
def root():
    return {'Message': 'Out Api'}


@router.post('/login')
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = ''
    for user in USER.find():
        if '_id' in user:
            del user['_id']
        if user.get(form.username):
            user_db = user[form.username]
            break
    if not user_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='username invalid')
    user = search_user_db(form.username)
    print('BOOL: ', crypt.verify(form.password, user.password))
    if not crypt.verify(form.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='password invalid')
    access_token = {"sub": user.username,
                    "exp": datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_DURATION)}
    print('ACCESS TOKEN: ', access_token)
    await send_token_authentication(access_token=jwt.encode(access_token, getenv('SECRET'), algorithm=ALGORITHM),
                                    email_receiver=user.email)
    return {"access_token": jwt.encode(access_token, getenv('SECRET'), algorithm=ALGORITHM), "token_type": "bearer"}


@router.post('/register')
async def register(user: UserDB):
    if search_user(user.username):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='The user already exist')
    if not is_valid_email(user.email):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='The email is invalid')
    user_info_dict = user.model_dump()
    user_info_dict['password'] = crypt.hash(str(user.password))
    user_info_dict = {f"{user.username}": user_info_dict}
    USER.insert_one(user_info_dict)
    access_token = {"sub": user.username,
                    "exp": datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_DURATION)}
    await send_token_authentication(access_token=jwt.encode(access_token, getenv('SECRET'), algorithm=ALGORITHM),
                                    email_receiver=user.email)
    return {"access_token": jwt.encode(access_token, getenv('SECRET'), algorithm=ALGORITHM), "token_type": "bearer"}


@router.get('/users/me')
async def me(user: Annotated[User, Depends(current_user)]):
    return user
