from logic.address import Address, address2


class Agency(BaseModel):
    """
     Class used to represent an Agency

     Attributes:
            id_agency (int): Id of the agency ( Used in the database ).
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

    id_agency: int = 0
    nit: int = 0
    business_name: str = "Business Name"
    contact: str = "Phone or E-mail"
    address: object = Address
    day: int = 1
    month: int = 1
    year: int = 1999
    date_actualization: date = date(year, month, day)

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
        return 'Id Agency: {0}, Nit: {1}, Business Name: {2}, Contact (Phone or E-mail): {3}, Address: {4}, ' \
               'Date Actualization: {5} - {6} - {7}'.format(self.id_agency, self.nit, self.business_name, self.contact,
                                                            self.address, self.day, self.month, self.year)


if __name__ == '__main__':
    # Prueba Agency class

    agency1 = Agency(id_agency=965816, nit=52173, business_name="Tiserium", contact="31459750", address=address2,
                     day=5, month=10, year=2023)

    agency2 = Agency(id_agency=965816, nit=52173, business_name="Tiserium", contact="31459750", address=address2,
                     day=5, month=10, year=2023)

    agency1_str = agency1.__str__()
    print(f"Agency 1 Information \n {agency1_str}")
    agency2_str = agency2.__str__()
    print(f"Agency 2 Information \n {agency2_str}")

    are_equal_agency = agency1.__eq__(agency2)
    print(f"Are equals ? \n {are_equal_agency} \n\n")

agency1 = Agency(id_agency=965816, nit=52173, business_name="Tiserium", contact="31459750", address=address2,
                 day=5, month=10, year=2023)

agency2 = Agency(id_agency=965816, nit=52173, business_name="Tiserium", contact="31459750", address=address2,
                 day=5, month=10, year=2023)
