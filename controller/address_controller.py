import json
import os
from typing import Union, List
from logic.flyweight_address import AddressFlyweightFactory
PATH = os.getcwd()
DIR_DATA = PATH + '{0}data{0}'.format(os.sep)
flyweight_add = AddressFlyweightFactory()


class AddressController(object):
    def __init__(self):
        self.file = '{0}{1}'.format(DIR_DATA, 'address.json')

    def add(self, shared_state: List[Union[int, str]],
            flyweight_address: AddressFlyweightFactory = AddressFlyweightFactory()) -> str:
        with open(self.file, 'r+') as f:
            data = json.load(f)
            data['address'].append(flyweight_address.__dict__)
            print(flyweight_address.__dict__)
            f.seek(0)
            json.dump(data, f)
        return flyweight_address.get_flyweight(shared_state=shared_state).__str__()

    def show(self):
        with open(self.file, 'r') as f:
            json_object = json.load(f)
        return json_object
