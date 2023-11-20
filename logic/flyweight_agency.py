from typing import List, Dict, Union
from pydantic import BaseModel
from logic.address import Address
from logic.agency_factory import AgencyFactory


class AgencyFlyweight(BaseModel):
    """
    Class representing a flyweight object for agencies.
    Attributes:
        shared_state (List[Union[str, int]]): Shared state of the agency.
        unique_state (Union[dict, None]): Unique state of the agency factory.
    Methods:
        __init__(**data): Initializes an AgencyFlyweight instance.
        operation(unique_state: dict) -> None: Performs an operation with the shared state and unique state.
    """
    shared_state: List[Union[str, int]] = []
    unique_state: Union[dict, None] = None

    def __init__(self, **data):
        """
        Initializes an AgencyFlyweight instance.
        Args:
            **data: Additional keyword arguments for initializing the instance.
        """
        super().__init__(**data)

    def operation(self, unique_state: dict) -> None:
        """
        Performs an operation with the shared state and unique state.
        Args:
            unique_state (dict): Unique state of the agency factory.
        """
        shared_state_str = ", ".join(str(self.shared_state))
        self.unique_state = unique_state
        print(f"AgencyFlyweight: Displaying shared ({shared_state_str}) "
              f"and unique ({list(self.unique_state.values())}) state.", end="")


def get_key(state: List[str]) -> str:
    """
    Get the key from the state.
    Args:
        state (List[str]): State.
    Returns:
        str: Generated key.
    """
    return "_".join(map(str, state))


class AgencyFlyweightFactory:
    """
    Class representing a factory for agency flyweight objects.
    Attributes:
        flyweights (Dict[str, AgencyFlyweight]): Dictionary to store flyweight objects.
    Methods:
        assign_flyweights(initial_flyweights: List[List[Union[str, int]]]) -> None: Assign initial flyweights.
        get_flyweight(shared_state: List[Union[str, int]]) -> AgencyFlyweight: Get a
                                                             flyweight object based on the shared state.
        list_flyweights() -> None: Display the list of available flyweights.
    """
    flyweights: Dict[str, AgencyFlyweight] = {}

    def assign_flyweights(self, initial_flyweights: List[List[Union[str, int]]]) -> None:
        """
        Assign initial flyweights.
        Args:
            initial_flyweights (List[List[Union[str, int]]]): List of initial states.
        """
        for state in initial_flyweights:
            key = get_key(state)
            agency = AgencyFlyweight()
            for data in state:
                agency.shared_state.append(data)
            self.flyweights[key] = agency

    def get_flyweight(self, shared_state: List[Union[str, int]]) -> AgencyFlyweight:
        """
        Get a flyweight object based on the shared state.
        Args:
            shared_state (List[Union[str, int]]): Shared state.
        Returns:
            AgencyFlyweight: Flyweight object.
        """
        key = get_key(shared_state)
        if not self.flyweights.get(key):
            print("AgencyFlyweightFactory: Can't find a flyweight, creating a new one.")
            self.flyweights[key] = AgencyFlyweight(shared_state=shared_state)
        else:
            print("AgencyFlyweightFactory: Reusing an existing flyweight.")
        return self.flyweights[key]

    def list_flyweights(self) -> None:
        """
        Display the list of available flyweights.
        """
        count = len(self.flyweights)
        print(f"AgencyFlyweightFactory: I have {count} flyweights:")
        print("\n".join(self.flyweights.keys()), end="")


def add_agency_to_database(
        factory_add: AgencyFlyweightFactory, id_entity: int, nit: int, business_name: str, contact: str,
        address: Address, day: int, month: int, year: int) -> None:
    """
    Add an agency to the database.
    Args:
        factory_add (AgencyFlyweightFactory): Flyweight factory.
        id_entity (int): Entity ID.
        nit (int): NIT.
        business_name (str): Business name.
        contact (str): Contact information.
        address (Address): Address of the agency.
        day (int): Day.
        month (int): Month.
        year (int): Year.
    """
    print("\n\nClient: Adding an agency to the database.")
    agency = AgencyFactory(id_entity=id_entity, nit=nit, business_name=business_name, contact=contact, address=address,
                           day=day, month=month, year=year)
    flyweight = factory_add.get_flyweight([id_entity, nit, business_name, contact, address.__str__(),
                                           day, month, year])
    flyweight.operation(agency.to_dict())
