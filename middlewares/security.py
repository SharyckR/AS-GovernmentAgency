from os import getenv
from typing import Union
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from typing_extensions import Annotated
from logic.legal_entity import LegalEntity
from logic.natural_entity import NaturalEntity
from logic.user_database import UserDB
oauth2 = OAuth2PasswordBearer(tokenUrl='/authentication/login')


async def auth_user(token: Annotated[str, Depends(oauth2)]):
    exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                              detail='Invalid authentication credentials',
                              headers={"WWW-Authenticate": "Bearer"})
    try:
        username = jwt.decode(token=token, key=getenv('SECRET'), algorithms=["HS256"]).get('sub')
        if username is None:
            print('Username is None')
            raise exception
    except JWTError as e:
        print('JTW Exception ', e)
        raise exception
    return UserDB.search_user(username)


async def current_user(user: Annotated[Union[NaturalEntity, LegalEntity], Depends(auth_user)]):
    if user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='The user is inactive')
    return user

