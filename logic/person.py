from pydantic import BaseModel
from logic.address import Address
from logic.education_history import EducationHistory


class Person(BaseModel):
    """
     Class used to represent a Person

     Attributes:
            id_person (int): Id of person ( used in the database ).
            type_id (str): Type id of person.
            dni (int): DNI of person.
            name (str): Name of person.
            last_name (str): Last name of person.
            phone (int): Phone of person.
            address (object): Address of person.
            education_history (object): Educational history of the person.
            mediator (object): Mediator for managing interactions.

        Methods:
            __str__(): Returns a string representation of a person.
            __eq__(other): Compares two objects person to check if they are equal.
    """

    id_person: int = 0
    type_id: str = ""
    dni: int = 0
    name: str = "Name"
    last_name: str = "LastName"
    phone: int = 0
    address: object = Address
    education_history: object = EducationHistory
    mediator: object = None

    def __init__(self, mediator=None, **data):
        super().__init__(**data)
        self.mediator = mediator

    def __eq__(self, another_person):
        """ Returns bool of equality of person objects.
        :returns: bool person
        :rtype: bool
        """
        return another_person.dni == self.dni

    def __str__(self):
        """ Returns str of person.
        :returns: string person
        :rtype: str
        """
        return 'Id Person: {0}, Type Id: {1}, Dni: {2}, Full name: {3} {4}, Phone: {5}, Address: {6}, ' \
               'Education History: {7}'.format(self.id_person, self.type_id, self.dni, self.name, self.last_name,
                                               self.phone, self.address, self.education_history)
