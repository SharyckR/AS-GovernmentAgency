from datetime import date
from pydantic import BaseModel
from logic.address import Address


class EducationHistory(BaseModel):
    """
     Class used to represent an Educational History

     Attributes:
            dni_person (int): DNI of the person to whom the history refers.
            education (str): Educational level of the person.
            name_institution (str): Name of the institution where the person studied.
            location (object): Location of the institution where the person studied.
            title_obtained (str): Title obtained by the person.
            day (int): Day component for date_graduation.
            month (int): Month component for date_graduation.
            year (int): Year component for date_graduation.
            date_graduation (datatime): Person's graduation date.
            mediator (object): Mediator for managing interactions.

        Methods:
            __str__(): Returns a string representation of an educational history.
            __eq__(other): Compares two objects educational history to check if they are equal.
    """

    dni_person: int = 0
    education: str = "Level of Education"
    name_institution: str = "Institution Name"
    location: object = Address
    title_obtained: str = "Title Obtained"
    day: int = 1
    month: int = 1
    year: int = 1999
    date_graduation: date = date(year, month, day)
    mediator: object = None

    def __init__(self, mediator=None, **data):
        super().__init__(**data)
        self.mediator = mediator

    def __eq__(self, another_history):
        """ Returns bool of equality of history objects.
        :returns: bool history
        :rtype: bool
        """
        return another_history.dni_person == self.dni_person

    def __str__(self):
        """ Returns str of educational history.
        :returns: string educational history
        :rtype: str
        """
        return 'Dni: {0}, Level of Education: {1}, Institution Name: {2}, Location: {3}, Title Obtained: {4}, ' \
               'Date Graduation: {5} - {6} - {7}'.format(self.dni_person, self.education, self.name_institution,
                                                         self.location, self.title_obtained, self.day,
                                                         self.year, self.month)
