from typing import List, Dict
from typing import Optional
from logic.address import Address, address1


class AddressFlyweight:
    def __init__(self, shared_state: List[str]) -> None:
        self._shared_state = shared_state

    def operation(self, unique_state: Address) -> None:
        shared_state_str = ", ".join(str(item) for item in self._shared_state)
        unique_state_str = str(unique_state)
        print(f"AddressFlyweight: Displaying shared ({shared_state_str}) and unique ({unique_state_str}) state.",
              end="")


def get_key(state: List[object]) -> str:
    state_str = [str(item) for item in state]
    return "_".join(state_str)


class AddressFlyweightFactory:
    _flyweights: Dict[str, AddressFlyweight] = {}

    def __init__(self, initial_flyweights: List[List[str]]) -> None:
        for state in initial_flyweights:
            key = get_key(state)
            self._flyweights[key] = AddressFlyweight(state)

    def get_flyweight(self, shared_state: List[str]) -> AddressFlyweight:
        key = get_key(shared_state)

        if not self._flyweights.get(key):
            print("AddressFlyweightFactory: Can't find a flyweight, creating a new one.")
            self._flyweights[key] = AddressFlyweight(shared_state)
        else:
            print("AddressFlyweightFactory: Reusing an existing flyweight.")

        return self._flyweights[key]

    def list_flyweights(self) -> None:
        count = len(self._flyweights)
        print(f"AddressFlyweightFactory: I have {count} flyweights:")
        print("\n".join(self._flyweights.keys()), end="")


def add_address_to_database(
    factory_add: AddressFlyweightFactory, street: str, number: Optional[int], apartment: Optional[int],
        postal_code: Optional[str], locality: str, department: str, country: str
) -> None:

    if apartment is None:
        apartment = "None"
    else:
        apartment = apartment

    print("\n\nClient: Adding an address to the database.")
    address = Address(street=street, number=number, apartment=apartment, postal_code=postal_code, locality=locality,
                      department=department, country=country)
    flyweight = factory_add.get_flyweight([street, number, apartment, postal_code, locality, department, country])
    flyweight.operation(address)


if __name__ == "__main__":
    factory = AddressFlyweightFactory([
        ["123 Main St", "5", "Apt 3B", "1010", "City Ville", "State Ville", "Country Land"],
        ["456 Elm St", "10", "None", "2020", "Towns Ville", "State Ville", "Country Land"],
        ["789 Oak St", "15", "Apt 2C", "3030", "Villa Getan", "State Ville", "Country Land"],
    ])

    factory.list_flyweights()

    add_address_to_database(
        factory, address1.street, address1.number, address1.apartment, address1.postal_code, address1.locality,
        address1.department, address1.country)

    add_address_to_database(
        factory, "456 Elm St", 10, None, '2020', "Towns Ville", "State Ville", "Country Land")

    print("\n")

    factory.list_flyweights()
