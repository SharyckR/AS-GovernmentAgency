from datetime import date
from pydantic import BaseModel
from logic.address import Address
from typing import Optional


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
    education: Optional[str] = "Level of Education"
    name_institution: Optional[str] = "Institution Name"
    location: Optional[object] = Address
    title_obtained: Optional[str] = "Title Obtained"
    day: Optional[int] = 1
    month: Optional[int] = 1
    year: Optional[int] = 1999
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

        education_str = str(self.education) if self.education is not None else "None"
        name_institution_str = str(self.name_institution) if self.name_institution is not None else "None"
        location_str = str(self.location) if self.location is not None else "None"
        title_obtained_str = str(self.title_obtained) if self.title_obtained is not None else "None"
        day_int = int(self.day) if self.day is not None else "None"
        month_int = int(self.month) if self.month is not None else "None"
        year_int = int(self.year) if self.year is not None else "None"
        
        return 'Dni: {0}, Level of Education: {1}, Institution Name: {2}, Location: {3}, Title Obtained: {4}, ' \
               'Date Graduation: {5} - {6} - {7}'.format(self.dni_person, education_str, name_institution_str,
                                                         location_str, title_obtained_str, day_int,
                                                         month_int, year_int)
