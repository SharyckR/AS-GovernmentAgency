from typing import Union
from pydantic import BaseModel


class Address(BaseModel):
    """
    Class to represent an address.

    Attributes:
        street (str): Street name.
        number (int): Address number.
        number (str): Address number.
        apartment (str): Apartment number.
        postal_code (str): Postal code.
        locality (str): City or locality.
        department (str): Department or state.
        country (str): Country.

    Methods:
        __str__(): Returns a string representation of the address.
        __eq__(other): Compares two addresses to check if they are equal.
    """
    street: str = 'street'
    number: int = 1
    apartment: Union[str, None] = 'apartment'
    postal_code: str = 'postal code'
    locality: str = 'locality'
    department: str = 'department'
    country: str = 'country'
    mediator: object = None

    def __init__(self, mediator=None, **data):
        super().__init__(**data)
        self.mediator = mediator

    def to_dict(self):
        apartment_str = str(self.apartment) if self.apartment is not None else "None"
        return {
            "street": self.street,
            "number": self.number,
            "apartment": apartment_str,
            "postal_code": self.postal_code,
            "locality": self.locality,
            "department": self.department,
            "country": self.country
        }

    def __str__(self):
        """
        Returns a string representation of the address.
        """
        apartment_str = str(self.apartment) if self.apartment is not None else "None"

        return ('(Street: {!r}, Number: {!r}, Apartment: {!r}, Postal Code: {!r}, '
                'Locality: {!r}, Department: {!r}, Country: {!r})').format(self.street, self.number, apartment_str,
                                                                           self.postal_code, self.locality,
                                                                           apartment_str, self.country)

    def __eq__(self, other):
        """
        Compares two addresses to check if they are equal.

        Args:
            other (Address): Another address to compare.

        Returns:
            bool: True if the addresses are equal, False otherwise.
        """
        if isinstance(other, Address):
            return (self.street == other.street and self.number == other.number and
                    self.apartment == other.apartment and
                    self.postal_code == other.postal_code and self.locality == other.locality and
                    self.department == other.department and self.country == other.country)
        else:
            return False


if __name__ == '__main__':
    # Prueba Address class

    address1 = Address(street='The cross', number=10, apartment='Apt 3B', postal_code='1010', locality='Aqueous',
                       department='Cundinamarca', country='Colombia')
    address2 = Address(street='The cross', number=10, apartment='Apt 5C', postal_code='1010', locality='Aqueous',
                       department='Cundinamarca', country='Colombia')

    address1_str = address1.__str__()
    print(f"Address 1 Information \n {address1_str}")
    address2_str = address2.__str__()
    print(f"Address 2 Information \n {address2}")

    are_equal_address = address1.__eq__(address2)
    print(f"Are equals ? \n {are_equal_address} \n\n")

address1 = Address(street='123 Main St', number=5, apartment='Apt 3B', postal_code='1010', locality='City Ville',
                   department='State Ville', country='Country Land')
address2 = Address(street='The cross', number=10, apartment='Apt 5C', postal_code='1010', locality='Aqueous',
                   department='Cundinamarca', country='Colombia')
