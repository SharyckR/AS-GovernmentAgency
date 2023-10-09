import json
from typing import List, Dict, Optional, Union
from logic.address import Address, address1


class AddressFlyweight:
    """
    Class representing a flyweight object for addresses.
    """
    def __init__(self, shared_state: List[Union[str, int]]) -> None:
        """
        Constructor for the AddressFlyweight class.
        Args:
            shared_state (List[Union[str, int]]): List of shared state.
        """
        self._shared_state = shared_state

    def operation(self, unique_state: Address) -> None:
        """
        Performs an operation with the shared state and unique state.
        Args:
            unique_state (Address): Unique state of the address.
        """
        shared_state_str = json.dumps(self._shared_state)
        unique_state_str = json.dumps(unique_state.__str__())
        print(f"AddressFlyweight: Displaying shared ({shared_state_str}) and unique ({unique_state_str}) state.",
              end="")


def get_key(state: List[Union[str, int]]) -> str:
    """
    Get the key from the state.
    Args:
        state (List[Union[str, int]]): State.
    Returns:
        str: Generated key.
    """
    return "_".join(map(str, state))


class AddressFlyweightFactory:
    """
    Class representing a factory for address flyweight objects.
    """
    _flyweights: Dict[str, AddressFlyweight] = {}

    def __init__(self, initial_flyweights: List[List[Union[str, int]]]) -> None:
        """
        Constructor for the AddressFlyweightFactory class.
        Args:
            initial_flyweights (List[List[Union[str, int]]]): List of initial states.
        """
        for state in initial_flyweights:
            key = get_key(state)
            self._flyweights[key] = AddressFlyweight(state)

    def get_flyweight(self, shared_state: List[Union[str, int]]) -> AddressFlyweight:
        """
        Get a flyweight object based on the shared state.
        Args:
            shared_state (List[Union[str, int]]): Shared state.
        Returns:
            AddressFlyweight: Flyweight object.
        """
        key = get_key(shared_state)
        if not self._flyweights.get(key):
            print("AddressFlyweightFactory: Can't find a flyweight, creating a new one.")
            self._flyweights[key] = AddressFlyweight(shared_state)
        else:
            print("AddressFlyweightFactory: Reusing an existing flyweight.")
        return self._flyweights[key]

    def list_flyweights(self) -> None:
        """
        Display the list of available flyweights.
        """
        count = len(self._flyweights)
        print(f"AddressFlyweightFactory: I have {count} flyweights:")
        print("\n".join(self._flyweights.keys()), end="")


def add_address_to_database(
        factory_add: AddressFlyweightFactory, street: str, number: int, apartment: Optional[str], postal_code: str,
        locality: str, department: str, country: str
) -> None:
    """
    Add an address to the database.
    Args:
        factory_add (AddressFlyweightFactory): Flyweight factory.
        street (str): Street.
        number (int): Number.
        apartment (Optional[str]): Apartment (optional).
        postal_code (str): Postal code.
        locality (str): Locality.
        department (str): Department.
        country (str): Country.
    """
    if apartment is None:
        apartment = "None"
    else:
        apartment = apartment

    print("\n\nClient: Adding an address to the database.")
    address = Address(street=street, number=number, apartment=apartment, postal_code=postal_code, locality=locality,
                      department=department, country=country)
    flyweight = factory_add.get_flyweight([street, str(number), apartment, postal_code, locality, department, country])
    flyweight.operation(address)
