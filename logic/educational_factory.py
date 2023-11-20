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
        create_agency(agency: AgencyFactory = AgencyFactory(),
                      education_histories: List[Union[EducationHistory, None]] = None) -> AbstractAgency:
            Create an instance of an EducationalAgency.
        create_history(**data) -> AbstractHistory:
            Create an instance of an EducationHistory.
    """
    def create_agency(self, agency: AgencyFactory = AgencyFactory(),
                      education_histories: List[Union[EducationHistory, None]] = None) -> AbstractAgency:
        """
        Create an instance of an EducationalAgency.
        Args:
            agency (AgencyFactory): The agency associated with the educational agency.
            education_histories (List[Union[EducationHistory, None]]): The education histories of the agency.
        Returns:
            AbstractAgency: An instance of EducationalAgency or its subclass.
        """
        if education_histories is None:
            education_histories = []
        return EducationalAgency(username=str(agency.id_entity), agency=agency, education_histories=education_histories)

    def create_history(self, **data) -> AbstractHistory:
        """
        Create an instance of an EducationHistory.
        Args:
            **data (dict): A dictionary containing the data for creating an EducationHistory.
        Returns:
            AbstractHistory: An instance of EducationHistory or its subclass.
        """
        return EducationHistory(**data)
