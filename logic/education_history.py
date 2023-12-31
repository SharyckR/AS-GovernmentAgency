from datetime import date
from pydantic import BaseModel
from logic.abstract_history import AbstractHistory
from logic.address import Address, address1, address2
from typing import Union, List


class EducationHistory(AbstractHistory, BaseModel):
    """
    Class used to represent an Educational History.
    Attributes:
        id_history (int): The identifier for the educational history.
        dni_person (int): DNI of the person to whom the history refers.
        education (Union[str, None]): Educational level of the person.
        name_institution (Union[str, None]): Name of the institution where the person studied.
        location (Union[Address, None]): Location of the institution where the person studied.
        title_obtained (Union[str, None]): Title obtained by the person.
        academic_achievements (List[Union[str, None]]): Academics achievements of the person.
        day (int): Day component for date_graduation.
        month (int): Month component for date_graduation.
        year (int): Year component for date_graduation.
        date_graduation (date): Person's graduation date.
        mediator (Union[object, None]): Mediator for managing interactions.
    Methods:
        __init__(mediator=None, **data): Initializes an EducationHistory object.
        to_dict(): Converts the educational history to a dictionary.
        __eq__(other): Compares two educational history objects to check if they are equal.
        __str__(): Returns a string representation of an educational history.
    """
    id_history: int = 1
    dni_person: int = 123456789
    education: Union[str, None] = "Level of Education"
    name_institution: Union[str, None] = "Institution Name"
    location: Union[Address, None] = Address()
    title_obtained: Union[str, None] = "Title Obtained"
    academic_achievements: List[Union[str, None]] = None
    day: int = 1
    month: int = 1
    year: int = 1999
    date_graduation: date = date(year, month, day)
    mediator: Union[object, None] = None

    def __init__(self, mediator=None, **data):
        """
        Initializes an EducationHistory object.
        Args:
            mediator: Mediator for managing interactions.
            **data: Additional data for education history attributes.
        """
        super().__init__(**data)
        self.mediator = mediator
        self.date_graduation = date(year=self.year, month=self.month, day=self.day)

    def to_dict(self):
        """
        Converts the educational history to a dictionary.
        Returns:
            dict: A dictionary representation of the educational history.
        """
        academic_achievements_str = self.academic_achievements if self.academic_achievements is not None else "None"
        education_str = str(self.education) if self.education is not None else "None"
        name_institution_str = str(self.name_institution) if self.name_institution is not None else "None"
        title_obtained_str = str(self.title_obtained) if self.title_obtained is not None else "None"
        return {
            str(self.dni_person): {
                "id_history": self.id_history, "education": education_str, "name_institution": name_institution_str,
                "location": self.location.to_dict(),  "title_obtained": title_obtained_str,
                "academic_achievements": academic_achievements_str,  "date_graduation": str(self.date_graduation)
            }
        }

    def __eq__(self, other):
        """
        Compares two educational history objects to check if they are equal.
        Args:
            other: Another EducationHistory object to compare.
        Returns:
            bool: True if the educational histories are equal, False otherwise.
        """
        if isinstance(other, EducationHistory):
            return (
                self.id_history == other.id_history
                and self.dni_person == other.dni_person
                and self.education == other.education
                and self.name_institution == other.name_institution
                and self.location == other.location
                and self.title_obtained == other.title_obtained
                and self.academic_achievements == other.academic_achievements
                and self.date_graduation == other.date_graduation
            )
        return False

    def __str__(self):
        """
        Returns a string representation of the educational history.
        Returns:
            str: A string representation of the educational history.
        """
        academic_achievements_str = self.academic_achievements if self.academic_achievements is not None else "None"
        education_str = str(self.education) if self.education is not None else "None"
        name_institution_str = str(self.name_institution) if self.name_institution is not None else "None"
        location_str = str(self.location) if self.location is not None else "None"
        title_obtained_str = str(self.title_obtained) if self.title_obtained is not None else "None"
        day_int = int(self.day) if self.day is not None else "None"
        month_int = int(self.month) if self.month is not None else "None"
        year_int = int(self.year) if self.year is not None else "None"
        return (
            'ID History: {!r}, DNI Person: {!r}, Level of Education: {!r}, Institution Name: {!r}, '
            'Location: {!r}, Title Obtained: {!r}, Academic Achievements: {!r}, '
            'Date Graduation: {!r} - {!r} - {!r}\n').format(
            self.id_history, self.dni_person, education_str, name_institution_str, location_str,
            title_obtained_str, academic_achievements_str,  day_int, month_int, year_int)


if __name__ == '__main__':
    # Test Educational History class
    edu_history1 = EducationHistory(
        id_history=40, dni_person=1043638720, education="Secondary", name_institution="Collage", location=address1,
        title_obtained="Graduated", academic_achievements=['Good Student'], day=13, month=10, year=2020)
    edu_history2 = EducationHistory(
        id_history=41, dni_person=45761873, education='Bachiller', name_institution='Institution Free',
        location=address2, title_obtained='Graduated', academic_achievements=['Good Student', 'Greate notes'],
        day=15,  month=12, year=2019)
    edu_history1_str = edu_history1.__str__()
    print(f"Education 1 Information \n {edu_history1_str}")
    edu_history2_str = edu_history2.__str__()
    print(f"Education 2 Information \n {edu_history2_str}")
    are_equal_edu_history = edu_history1.__eq__(edu_history2)
    print(f"Are equals ? \n {are_equal_edu_history} \n\n")
    
edu_history1 = EducationHistory(
        id_history=40, dni_person=1043638720, education="Secondary", name_institution="Collage", location=address1,
        title_obtained="Graduated", academic_achievements=['Good Student'], day=13, month=10, year=2020)
edu_history2 = EducationHistory(
        id_history=41, dni_person=45761873, education='Bachiller', name_institution='Institution Free',
        location=address2,  title_obtained='Graduated', academic_achievements=['Good Student', 'Greate notes'],
        day=15, month=12, year=2019)
