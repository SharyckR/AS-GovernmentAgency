from typing import Any
from logic.abstract_agency import AbstractAgency
from logic.address import Address, address2, address1
from logic.legal_entity import LegalEntity
from datetime import date


class AgencyFactory(AbstractAgency, LegalEntity):
    """
    Class used to represent an Agency.
    Attributes:
        id_entity (int): ID of the agency (Used in the database).
        entity (LegalEntity): LegalEntity object representing the entity type.
        nit (int): NIT of the agency.
        business_name (str): Name of the agency.
        contact (str): Contact information of the agency (phone number or email).
        address (Address): Address of the agency.
        day (int): Day component for date_actualization.
        month (int): Month component for date_actualization.
        year (int): Year component for date_actualization.
        date_actualization (date): Date on which the data is updated or displayed.
    Methods:
        __init__(**data: Any): Initializes an AgencyFactory object.
        to_dict(): Converts the agency to a dictionary.
        __eq__(another_agency): Compares two agency objects to check if they are equal.
        __str__(): Returns a string representation of the agency.
    """
    id_entity: int = 1
    entity: LegalEntity = LegalEntity()
    nit: int = 0
    business_name: str = "Business Name"
    contact: str = "Phone or E-mail"
    address: Address = Address()
    day: int = 1
    month: int = 1
    year: int = 1999
    date_actualization: date = date(year, month, day)

    def __init__(self, **data: Any):
        """
        Initializes an AgencyFactory object.
        Args:
            **data: Additional data for agency attributes.
        """
        super().__init__(**data)
        self.date_actualization = date(year=self.year, month=self.month, day=self.day)

    def to_dict(self):
        """
        Converts the agency to a dictionary.
        Returns:
            dict: A dictionary representation of the agency.
        """
        return {
            'id_entity': self.id_entity,
            'entity': self.entity.to_dict(),
            'nit': self.nit,
            'business_name': self.business_name,
            'contact': self.contact,
            'address': self.address.to_dict(),
            'date_actualization': str(self.date_actualization)
        }

    def __eq__(self, another_agency):
        """
        Compares two agency objects to check if they are equal.
        Args:
            another_agency: Another AgencyFactory object to compare.
        Returns:
            bool: True if the agencies are equal, False otherwise.
        """
        return another_agency.nit == self.nit

    def __str__(self):
        """
        Returns a string representation of the agency.
        Returns:
            str: A string representation of the agency.
        """
        return ('Id Agency: {0}, Entity: Type: {1}, Nit: {2}, Business Name: {3}, Contact (Phone or E-mail): {4}, '
                'Address: {5}, Date Actualization: {6} - {7} - {8}\n').format(self.id_entity, self.entity.type,
                                                                              self.nit, self.business_name,
                                                                              self.contact,
                                                                              self.address.__str__(), self.day,
                                                                              self.month, self.year)


if __name__ == '__main__':
    # Test AgencyFactory class
    agency1 = AgencyFactory(
        username='10290294', id_entity=965816, entity=LegalEntity(), nit=52173, business_name="Business Name",
        contact="31459750", address=address2, day=5, month=10, year=2023)
    agency2 = AgencyFactory(
        username='965816', id_entity=965816, entity=LegalEntity(), nit=52173, business_name="Business Name",
        contact="31459750", address=address2, day=5, month=10, year=2023)
    agency1_str = agency1.__str__()
    print(f"Agency 1 Information \n {agency1_str}")
    agency2_str = agency2.__str__()
    print(f"Agency 2 Information \n {agency2_str}")
    are_equal_agency = agency1.__eq__(agency2)
    print(f"Are equals ? \n {are_equal_agency} \n\n")

agency1 = AgencyFactory(username='965816', id_entity=965816, entity=LegalEntity(), nit=52173,
                        business_name="Tis er ium", contact="3145975012", address=address1, day=5, month=10, year=2023)
agency2 = AgencyFactory(username='10290294', id_entity=10290294, entity=LegalEntity(), nit=4224,
                        business_name="Business Name", contact="31459750", address=address2, day=5, month=10, year=2023)
