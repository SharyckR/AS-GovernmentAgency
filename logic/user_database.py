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
    """
    Represents a user in the database.
    Attributes:
        password (Union[str, int]): The password associated with the user.
    Methods:
        __init__(**data):
            Initializes a UserDB object.
        search_user(username: str) -> Union[NaturalEntity, LegalEntity]:
            Searches for a user in the database and returns a NaturalEntity or LegalEntity object.
        search_user_db(username: str) -> UserDB:
            Searches for a user in the database and returns a UserDB object.
    """
    password: Union[str, int] = "password"

    def __init__(self, **data):
        """
        Initializes a UserDB object.
        Args:
            **data: Additional data to initialize the object.
        """
        super().__init__(**data)
        if "password" not in data:
            self.password = self.username

    @classmethod
    def search_user(cls, username: str) -> Union[NaturalEntity, LegalEntity]:
        """
        Searches for a user in the database and returns a NaturalEntity or LegalEntity object.
        Args:
            username (str): The username to search for.
        Returns:
            Union[NaturalEntity, LegalEntity]: A NaturalEntity or LegalEntity object representing the user.
        """
        for user in NATURAL.find():
            if user.get(username):
                user_data = user.get(username)
                return NaturalEntity(**user_data)
        for user in LEGAL.find():
            if user.get(username):
                user_data = user.get(username)
                return LegalEntity(**user_data)

    @classmethod
    def search_user_db(cls, username: str) -> "UserDB":
        """
        Searches for a user in the database and returns a UserDB object.
        Args:
            username (str): The username to search for.
        Returns:
            UserDB: A UserDB object representing the user.
        """
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
