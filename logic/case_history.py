from datetime import date
from pydantic import BaseModel
from typing import Optional


class CaseHistory(BaseModel):
    """
     Class used to represent a Medical History

     Attributes:
            dni_person (int): DNI of the person to whom the history refers.
            case (str): Attribute that stores the case name
            arrested (char): Has the person ever been arrested?
            description_case (str): Type a description of the person's case
            jurisdiction (str): Attribute that saves the jurisdiction of the case
            date_arrested (datatime):Enter the date the person was arrested

            mediator (object): Mediator for managing interactions.

        Methods:
            __str__(): Returns a string representation of a case history.
            __eq__(other): Compares two objects case history to check if they are equal.
    """

    dni_person: int = 0
    case: str = "Name case"
    arrested: str = "Yes or No"
    description_case: Optional[str] = "Description of case"
    jurisdiction: Optional[str] = "Jurisdiction of the case"
    day: Optional[int] = 1
    month: Optional[int] = 1
    year: Optional[int] = 1999
    date_arrested: Optional[date] = date(year, month, day)
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
        """ Returns str of case history.
        :returns: string case history
        :rtype: str
        """
        description_case_str = str(self.description_case) if self.description_case is not None else "None"
        jurisdiction_str = str(self.jurisdiction) if self.jurisdiction is not None else "None"
        day_int = int(self.day) if self.day is not None else "None"
        month_int = int(self.month) if self.month is not None else "None"
        year_int = int(self.year) if self.year is not None else "None"

        return 'Dni: {0}, Case: {1}, Arrested: {2}, Description of case: {3}, Jurisdiction: {4}, ' \
               'Date arrested: {5} - {6} - {7}'.format(self.dni_person, self.case, self.arrested, description_case_str,
                                                       jurisdiction_str, year_int, month_int, day_int)
