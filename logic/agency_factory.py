from logic.abstract_agency import AbstractAgency
from logic.address import Address, address2, address1
from logic.legal_entity import LegalEntity
from datetime import date


class AgencyFactory(AbstractAgency, LegalEntity):
    """
     Class used to represent an Agency

     Attributes:
            id_entity (int): Id of the agency ( Used in the database ).
            nit (str): NIT of agency.
            business_name (str): Name of agency.
            contact (int): Contact of agency ( It could be a phone number or email ).
            address (object): Address of agency.
            day (int): Day component for date_actualization.
            month (int): Month component for date_actualization.
            year (int): Year component for date_actualization.
            date_actualization (object): Date on which the data is updated or displayed.

        Methods:
            __str__(): Returns a string representation of an agency.
            __eq__(other): Compares two objects agency to check if they are equal.
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

    def actualization_date(self, day: int, month: int, year: int):
        self.date_actualization = date(year=year, month=month, day=day)

    def to_dict(self):
        return {
            'ID Entity': self.id_entity,
            'Entity': self.entity.type,
            'NIT': self.nit,
            'Business Name': self.business_name,
            'Contact': self.contact,
            'Address': self.address.to_dict(),
            'Date Actualization': str(self.date_actualization)
        }

    def __eq__(self, another_agency):
        """ Returns bool of equality of agency objects.
        :returns: bool agency
        :rtype: bool
        """
        return another_agency.nit == self.nit

    def __str__(self):
        """ Returns str of agency.
        :returns: string agency
        :rtype: str
        """
        return 'Id Agency: {0}, Entity: Type: {1}, Nit: {2}, Business Name: {3}, Contact (Phone or E-mail): {4}, ' \
               'Address: {5}, Date Actualization: {6} - {7} - {8}'.format(self.id_entity, self.entity.type,
                                                                          self.nit, self.business_name, self.contact,
                                                                          self.address.__str__(), self.day, self.month,
                                                                          self.year)


if __name__ == '__main__':
    # Prueba Agency class

    agency1 = AgencyFactory(id_entity=965816, entity=LegalEntity(), nit=52173, business_name="Business Name",
                            contact="31459750", address=address2, day=5, month=10, year=2023)

    agency2 = AgencyFactory(id_entity=965816, entity=LegalEntity(), nit=52173, business_name="Business Name",
                            contact="31459750", address=address2, day=5, month=10, year=2023)

    agency1_str = agency1.__str__()
    print(f"Agency 1 Information \n {agency1_str}")
    agency2_str = agency2.__str__()
    print(f"Agency 2 Information \n {agency2_str}")

    are_equal_agency = agency1.__eq__(agency2)
    print(f"Are equals ? \n {are_equal_agency} \n\n")

agency1 = AgencyFactory(id_entity=965816, entity=LegalEntity(), nit=52173, business_name="Tis er ium",
                        contact="3145975012", address=address1, day=5, month=10, year=2023)

agency2 = AgencyFactory(id_entity=10290294,  entity=LegalEntity(), nit=4224, business_name="Business Name",
                        contact="31459750", address=address2, day=5, month=10, year=2023)
