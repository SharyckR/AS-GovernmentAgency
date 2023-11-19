from os import getenv
from typing import Union
from pymongo import MongoClient
from logic.legal_entity import LegalEntity
from logic.natural_entity import NaturalEntity
MY_CLIENT = MongoClient(getenv('MONGODB_CONNECTION_STRING'))
USERS = MY_CLIENT['USERS']
NATURAL = USERS['Natural']
LEGAL = USERS['Legal']


class UserDB(LegalEntity, NaturalEntity):
    password: Union[str, int] = "password"

    def __init__(self, **data):
        super().__init__(**data)
        if "password" not in data:
            self.password = self.username

    @classmethod
    def search_user(cls, username: str):
        for user in NATURAL.find():
            if user.get(username):
                user_data = user.get(username)
                return NaturalEntity(**user_data)
        for user in LEGAL.find():
            if user.get(username):
                user_data = user.get(username)
                return NaturalEntity(**user_data)

    @classmethod
    def search_user_db(cls, username: str):
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
