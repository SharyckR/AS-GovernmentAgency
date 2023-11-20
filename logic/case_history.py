from datetime import date
from pydantic import BaseModel
from typing import Union
from logic.abstract_history import AbstractHistory


class CaseHistory(AbstractHistory, BaseModel):
    """
    Class used to represent a Medical History.
    Attributes:
        id_history (int): ID of the case history.
        dni_person (int): DNI of the person to whom the history refers.
        case (str): Attribute that stores the case name.
        arrested (str): Has the person ever been arrested? (Yes or No)
        description_case (Union[str, None]): Type a description of the person's case.
        jurisdiction (Union[str, None]): Attribute that saves the jurisdiction of the case.
        day (int): Day component for date_arrested.
        month (int): Month component for date_arrested.
        year (int): Year component for date_arrested.
        date_arrested (date): Enter the date the person was arrested.
        lawyer (Union[str, None]): Lawyer in charge.
        mediator (Union[object, None]): Mediator for managing interactions.
    Methods:
        __init__(mediator=None, **data): Initializes a CaseHistory object.
        to_dict(): Converts the case history to a dictionary.
        __eq__(other): Compares two case history objects to check if they are equal.
        __str__(): Returns a string representation of the case history.
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
    lawyer: Union[str, None] = "Lawyer in Charge"
    mediator: Union[object, None] = None

    def __init__(self, mediator=None, **data):
        """
        Initializes a CaseHistory object.
        Args:
            mediator: Mediator for managing interactions.
            **data: Additional data for case history attributes.
        """
        super().__init__(**data)
        self.mediator = mediator
        self.date_arrested = date(year=self.year, month=self.month, day=self.day)

    def to_dict(self):
        """
        Converts the case history to a dictionary.
        Returns:
            dict: A dictionary representation of the case history.
        """
        description_case_str = str(self.description_case) if self.description_case is not None else "None"
        jurisdiction_str = str(self.jurisdiction) if self.jurisdiction is not None else "None"
        lawyer_str = str(self.lawyer) if self.lawyer is not None else "None"
        return {
            str(self.dni_person): {"id_history": self.id_history, "case": self.case, "arrested": self.arrested,
                                   "description_case": description_case_str, "jurisdiction": jurisdiction_str,
                                   "date_arrested": str(self.date_arrested), "lawyer": lawyer_str}}

    def __eq__(self, other):
        """
        Compares two case history objects to check if they are equal.
        Args:
            other: Another CaseHistory object to compare.
        Returns:
            bool: True if the case histories are equal, False otherwise.
        """
        if isinstance(other, CaseHistory):
            return (self.id_history == other.id_history and self.dni_person == other.dni_person
                    and self.case == other.case and self.arrested == other.arrested
                    and self.description_case == other.description_case and self.jurisdiction == other.jurisdiction
                    and self.day == other.day and self.month == other.month and self.year == other.year
                    and self.date_arrested == other.date_arrested and self.lawyer == other.lawyer)
        return False

    def __str__(self):
        """
        Returns a string representation of the case history.
        Returns:
            str: A string representation of the case history.
        """
        description_case_str = str(self.description_case) if self.description_case is not None else "None"
        jurisdiction_str = str(self.jurisdiction) if self.jurisdiction is not None else "None"
        day_int = int(self.day) if self.day is not None else "None"
        month_int = int(self.month) if self.month is not None else "None"
        year_int = int(self.year) if self.year is not None else "None"
        lawyer_str = str(self.lawyer) if self.lawyer is not None else "None"
        return (
            'ID History: {!r}, DNI Person: {!r}, Case: {!r}, Arrested: {!r}, Description of case: {!r}, '
            'Jurisdiction: {!r}, Date arrested: {!r} - {!r} - {!r}, Lawyer in Charge: {!r}\n').format(
            self.id_history, self.dni_person, self.case, self.arrested, description_case_str, jurisdiction_str,
            year_int, month_int, day_int, lawyer_str)


if __name__ == '__main__':
    # Test CaseHistory class
    case_history1 = CaseHistory(
        dni_person=1043638720, case="Heist", arrested="Yes", description_case="Stole a necklace",
        jurisdiction="Disciplinary", day=15, year=2021, month=5, lawyer="Cristian Arroyo")
    case_history2 = CaseHistory(
        dni_person=45761873, case="Public disturbance", arrested="No", description_case=None, jurisdiction=None,
        day=4, month=10, year=2020, lawyer=None)
    case_history1_str = case_history1.__str__()
    print(f"Case History 1 Information \n {case_history1_str}")
    case_history2_str = case_history2.__str__()
    print(f"Case History 2 Information \n {case_history2_str}")
    are_equal_case_history = case_history1.__eq__(case_history2)
    print(f"Are equals ? \n {are_equal_case_history} \n\n")

case_history1 = CaseHistory(
    id_history=13, dni_person=1043638720, case="Heist", arrested="Yes", description_case="Stole a necklace",
    jurisdiction="Disciplinary", day=15, year=2021, month=5, lawyer="Cristian Arroyo")
case_history2 = CaseHistory(
    id_history=14, dni_person=45761873, case="Public disturbance", arrested="No", description_case=None,
    jurisdiction=None, day=6, year=7, month=4, lawyer=None)
