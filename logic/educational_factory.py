from datetime import date
from typing import List, Optional
from logic.abstract_factory import AbstractFactory
from logic.abstract_agency import AbstractAgency
from logic.abstract_history import AbstractHistory
from logic.agency_factory import AgencyFactory
from logic.education_history import EducationHistory
from logic.educational_agency import EducationalAgency


class EducationalFactory(AbstractFactory):
    """
    Concrete factory for creating educational agency and history objects.

    Attributes:
        None

    Methods:
        create_agency(agency: AgencyFactory = AgencyFactory, education_history: EducationHistory = None,
                      academic_achievements: List[str] = None) -> AbstractAgency:
            Create an instance of an EducationalAgency.

        create_history(dni_person: int = None, education: Optional[str] = None,
                       name_institution: Optional[str] = None, location: Optional[object] = None,
                       title_obtained: Optional[str] = None, day: Optional[int] = None,
                       month: Optional[int] = None, year: Optional[int] = None, date_graduation: date = None,
                       mediator: object = None) -> AbstractHistory:
            Create an instance of an EducationHistory.
    """
    def create_agency(self, agency: AgencyFactory = AgencyFactory, education_history: EducationHistory = None,
                      academic_achievements: List[str] = None) -> AbstractAgency:
        """
        Create an instance of an EducationalAgency.

        Args:
            agency (AgencyFactory): The agency associated with the educational agency.
            education_history (EducationHistory): The education history of the agency.
            academic_achievements (List[str]): List of academic achievements.

        Returns:
            AbstractAgency: An instance of EducationalAgency or its subclass.
        """
        return EducationalAgency(agency=agency, education_history=education_history,
                                 academic_achievements=academic_achievements)

    def create_history(self, dni_person: int = None, education: Optional[str] = None,
                       name_institution: Optional[str] = None, location: Optional[object] = None,
                       title_obtained: Optional[str] = None, day: Optional[int] = None,
                       month: Optional[int] = None, year: Optional[int] = None, date_graduation: date = None,
                       mediator: object = None) -> AbstractHistory:
        """
        Create an instance of an EducationHistory.

        Args:
            dni_person (int): The DNI of the person with the education history.
            education (str): Educational background information.
            name_institution (str): Name of the educational institution.
            location (object): Location information.
            title_obtained (str): Title obtained.
            day (int): Day of graduation.
            month (int): Month of graduation.
            year (int): Year of graduation.
            date_graduation (date): Date of graduation.
            mediator (object): Mediator object.

        Returns:
            AbstractHistory: An instance of EducationHistory or its subclass.
        """
        return EducationHistory(dni_person=dni_person, education=education, name_institution=name_institution,
                                location=location, title_obtained=title_obtained, day=day, month=month, year=year,
                                date_graduation=date_graduation, mediator=mediator)
