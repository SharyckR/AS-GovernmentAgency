import json
from typing import List, Dict, Union
from pydantic import BaseModel


class AddressFlyweight(BaseModel):
    """
    Class representing a flyweight object for addresses.

    Attributes:
        shared_state (List[Union[str, int]]): Shared state of the address.
        unique_state (Union[dict, None]): Unique state of the address.

    Methods:
        operation(unique_state: dict) -> None:
            Performs an operation with the shared state and unique state.
        __str__() -> str:
            Returns a string representation of the shared state.
        to_dict() -> dict:
            Returns a dictionary representation of the shared state.
    """
    shared_state: List[Union[str, int]] = []
    unique_state: Union[dict, None] = None

    def operation(self, unique_state: dict) -> None:
        """
        Performs an operation with the shared state and unique state.
        Args:
            unique_state (dict): Unique state of the address.
        """
        shared_state_str = json.dumps(str(self.shared_state))
        self.unique_state = unique_state
        print(f"AddressFlyweight: Displaying shared ({shared_state_str}) "
              f"and unique ({list(self.unique_state.values())}) state.", end="")

    def __str__(self) -> str:
        """
        Returns a string representation of the shared state.
        Returns:
            str: String representation of the shared state.
        """
        return f'{self.shared_state}'

    def to_dict(self) -> dict:
        """
        Returns a dictionary representation of the shared state.
        Returns:
            dict: Dictionary representation of the shared state.
        """
        return {
            "street": self.shared_state[0], "number": self.shared_state[1], "apartment": self.shared_state[2],
            "postal_code": self.shared_state[3], "locality": self.shared_state[4], "department": self.shared_state[5],
            "country": self.shared_state[6]
        }


def get_key(state: List[Union[str, int]]) -> str:
    """
    Get the key from the state.
    Args:
        state (List[Union[str, int]]): State.
    Returns:
        str: Generated key.
    """
    return "_".join(map(str, state))


class AddressFlyweightFactory(BaseModel):
    """
    Class representing a factory for address flyweight objects.
    Attributes:
        flyweights (Dict[str, AddressFlyweight]): Dictionary to store flyweight objects.
    Methods:
        __init__(**data) -> None:
            Initializes an AddressFlyweightFactory instance.
        assign_flyweights(initial_flyweights: List[List[Union[str, int]]]) -> None:
            Assign initial flyweights.
        get_flyweight(shared_state: List[Union[str, int]]) -> AddressFlyweight:
            Get a flyweight object based on the shared state.
        check_flyweight(shared_state: List[Union[str, int]]) -> bool:
            Check if a flyweight object based on the shared state exists.
        list_flyweights() -> int:
            Display the list of available flyweights.
    """
    flyweights: Dict[str, AddressFlyweight] = {}

    def __init__(self, **data):
        """
        Initializes an AddressFlyweightFactory instance.
        Args:
            **data: Additional keyword arguments for initializing the instance.
        """
        super().__init__(**data)

    def assign_flyweights(self, initial_flyweights: List[List[Union[str, int]]]) -> None:
        """
        Assign initial flyweights.
        Args:
            initial_flyweights (List[List[Union[str, int]]]): List of initial states.
        """
        for state in initial_flyweights:
            key = get_key(state)
            self.flyweights[key] = AddressFlyweight(shared_state=state)

    def get_flyweight(self, shared_state: List[Union[str, int]]) -> AddressFlyweight:
        """
        Get a flyweight object based on the shared state.
        Args:
            shared_state (List[Union[str, int]]): Shared state.
        Returns:
            AddressFlyweight: Flyweight object.
        """
        key = get_key(shared_state)
        print('Key ', key)
        if not self.flyweights.get(key):
            print("AddressFlyweightFactory: Can't find a flyweight, creating a new one.")
            self.flyweights[key] = AddressFlyweight(shared_state=shared_state)
        else:
            print("AddressFlyweightFactory: Reusing an existing flyweight.")
        return self.flyweights[key]

    def check_flyweight(self, shared_state: List[Union[str, int]]) -> bool:
        """
        Check if a flyweight object based on the shared state exists.
        Args:
            shared_state (List[Union[str, int]]): Shared state.
        Returns:
            bool: True if the flyweight object exists, False otherwise.
        """
        key = get_key(shared_state)
        print('Key: ', key)
        if not self.flyweights.get(key):
            print("Data does not exist in the database.")
            return False
        else:
            print("Data exists in the database.")
            return True

    def list_flyweights(self) -> int:
        """
        Display the list of available flyweights.
        Returns:
            int: Number of available flyweights.
        """
        count = len(self.flyweights)
        print(f"AddressFlyweightFactory: I have {count} flyweights:")
        print("\n".join(self.flyweights.keys()), "\n", end="")
        return count


def add_address_to_database(factory_add: AddressFlyweightFactory, data: dict) -> None:
    """
    Add an address to the database.
    Args:
        factory_add (AddressFlyweightFactory): AddressFlyweightFactory instance.
        data (dict): Data representing the address.
    """
    data['apartment'] = "None" if data['apartment'] is None else data['apartment']
    print("\n\nClient: Adding an address to the database.")
    flyweight = factory_add.get_flyweight(list(data.values()))
    print(flyweight.shared_state)
