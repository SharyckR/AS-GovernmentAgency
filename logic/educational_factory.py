from typing import List, Union
from logic.abstract_factory import AbstractFactory
from logic.abstract_agency import AbstractAgency
from logic.abstract_history import AbstractHistory
from logic.agency_factory import AgencyFactory
from logic.education_history import EducationHistory
from logic.educational_agency import EducationalAgency


class EducationalFactory(AbstractFactory):
    """
    Concrete factory for creating educational agency and history objects.
    Methods:
        create_agency(agency: AgencyFactory = AgencyFactory(), education_history: EducationHistory = None,
                      academic_achievements: List[str] = None) -> AbstractAgency:
            Create an instance of an EducationalAgency.

        create_history(id_history: int = 1, dni_person: int = 1, education: Union[str, None] = None,
        name_institution: Union[str, None] = None, location: Union[Address, None] = Address(), title_obtained: Union[
        str, None] = None, day: Union[int, None] = None, month: Union[int, None] = None, year: Union[int,
        None] = None, date_graduation: Union[date, None] = None, mediator: Union[object, None] = None) ->
        AbstractHistory: Create an instance of an EducationHistory.
    """
    def create_agency(self, agency: AgencyFactory = AgencyFactory(),
                      education_histories: List[Union[EducationHistory, None]] = None
                      ) -> AbstractAgency:
        """
        Create an instance of an EducationalAgency.
        Args:
            agency (AgencyFactory): The agency associated with the educational agency.
            education_histories (List): The education histories of the agency.
        Returns:
            AbstractAgency: An instance of EducationalAgency or its subclass.
        """
        if education_histories is None:
            education_histories = [EducationHistory()]
        return EducationalAgency(username=str(agency.id_entity), agency=agency, education_histories=education_histories)

    def create_history(self, **data) -> AbstractHistory:
        """
        Create an instance of an EducationHistory.
        Args:
            data (dict): A dictionary containing the data for creating an EducationHistory.

        Returns:
            AbstractHistory: An instance of EducationHistory or its subclass.
        """
        return EducationHistory(**data)
