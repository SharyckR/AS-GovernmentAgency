from os import getenv
from dotenv import load_dotenv
from pymongo import MongoClient
from logic.flyweight_address import AddressFlyweightFactory
from typing import List, Union

load_dotenv()
MY_CLIENT = MongoClient(getenv('MONGODB_CONNECTION_STRING'))

ADDRESS = MY_CLIENT['Location']
COL_ADDRESS = ADDRESS['Address']

"""
def get_one_address(street, number, apartment, postalcode, locality, department, country):
    address_data = COL_ADDRESS.find_one({"street": street}, {"number": number}, {"apartment": apartment},
                                        {"postal_code": postalcode}, {"locality": locality},
                                        {"department": department}, {"country": country})
    return address_data"""


class FlyAddressController:

    def __init__(self):
        """
        :rtype: object
        """
        self._factory: AddressFlyweightFactory = AddressFlyweightFactory()

    def load_data(self):
        self._factory.flyweights = {}
        for address in COL_ADDRESS.find():
            if '_id' in address:
                del address['_id']
            self._factory.get_flyweight(list(address.values()))

    def check_database(self, data_to_check: List[Union[str, int]]) -> bool:
        flyweight = self._factory.check_flyweight(data_to_check)
        if flyweight:
            return True
        else:
            return False

    def get_address(self):
        self.load_data()
        if self._factory.list_flyweights() == 0:
            raise Exception('No data yet')
        return self._factory.flyweights

    def add_address_to_database(self, data: dict) -> None:
        self.load_data()
        print("\n\nClient: Adding an address to the database\n ...\n")
        if self._factory.check_flyweight(list(data.values())):
            raise Exception('The data is already in the database\n')
        else:
            COL_ADDRESS.insert_one(self._factory.get_flyweight(list(data.values())).to_dict())
            print('Data added\n')
