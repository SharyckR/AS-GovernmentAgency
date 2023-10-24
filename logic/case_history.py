from datetime import date
from pydantic import BaseModel
from typing import Union
from logic.abstract_history import AbstractHistory


class CaseHistory(AbstractHistory, BaseModel):
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
    id_history: int = 1
    dni_person: int = 123456789
    case: str = "Name case"
    arrested: str = "Yes or No"
    description_case: Union[str, None] = "Description of case"
    jurisdiction: Union[str, None] = "Jurisdiction of the case"
    day: int = 1
    month: int = 1
    year: int = 1999
    date_arrested: date = date(year, month, day)
    mediator: Union[object, None] = None

    def __init__(self, mediator=None, **data):
        super().__init__(**data)
        self.mediator = mediator
        self.date_arrested = date(year=self.year, month=self.month, day=self.day)

    def to_dict(self):
        description_case_str = str(self.description_case) if self.description_case is not None else "None"
        jurisdiction_str = str(self.jurisdiction) if self.jurisdiction is not None else "None"
        return {
            "id_history": self.id_history,
            "dni_person": self.dni_person,
            "case": self.case,
            "arrested": self.arrested,
            "description_case": description_case_str,
            "jurisdiction": jurisdiction_str,
            "date_arrested": str(self.date_arrested)
        }

    def __eq__(self, other):
        """ Returns bool of equality of history objects.
        :returns: bool history
        :rtype: bool
        """
        if isinstance(other, CaseHistory):
            return (self.id_history == other.id_history and self.dni_person == other.dni_person and
                    self.case == other.case and self.arrested == other.arrested and
                    self.description_case == other.description_case and self.jurisdiction == other.jurisdiction and
                    self.day == other.day and self.month == other.month and
                    self.year == other.year and self.date_arrested == other.date_arrested)
        return False

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

        return ('ID History: {0}, DNI Person: {1}, Case: {2}, Arrested: {3}, Description of case: {4}, '
                'Jurisdiction: {5}, Date arrested: {6} - {7} - {8}').format(
            self.id_history, self.dni_person, self.case, self.arrested, description_case_str, jurisdiction_str,
            year_int, month_int, day_int)


if __name__ == '__main__':
    # Prueba Case History class

    case_history1 = CaseHistory(dni_person=1043638720, case="Heist", arrested="Yes",
                                description_case="Stole a necklace", jurisdiction="Disciplinary", day=15, year=2021,
                                month=5)

    case_history2 = CaseHistory(dni_person=45761873, case="Public disturbance", arrested="No",
                                description_case=None, jurisdiction=None, day=4, month=10, year=2020)

    case_history1_str = case_history1.__str__()
    print(f"Case History 1 Information \n {case_history1_str}")
    case_history2_str = case_history2.__str__()
    print(f"Case History 2 Information \n {case_history2_str}")

    are_equal_case_history = case_history1.__eq__(case_history2)
    print(f"Are equals ? \n {are_equal_case_history} \n\n")

case_history1 = CaseHistory(id_history=13, dni_person=1043638720, case="Heist", arrested="Yes",
                            description_case="Stole a necklace", jurisdiction="Disciplinary", day=15, year=2021,
                            month=5)

case_history2 = CaseHistory(id_history=14, dni_person=45761873, case="Public disturbance", arrested="No",
                            description_case=None, jurisdiction=None, day=6, year=7, month=4)
