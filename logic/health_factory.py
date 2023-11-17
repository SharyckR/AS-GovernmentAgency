from typing import List, Union

from logic.abstract_factory import AbstractFactory
from logic.abstract_agency import AbstractAgency
from logic.abstract_history import AbstractHistory
from logic.agency_factory import AgencyFactory
from logic.health_agency import HealthAgency
from logic.medical_history import MedicalHistory


class HealthFactory(AbstractFactory):
    """
    Concrete factory for creating health agency and history objects.
    Methods:
        create_agency(agency: Agency = None, medical_history: MedicalHistory = None) -> AbstractAgency:
            Create an instance of a HealthAgency.
        create_history(dni_person: int = None, type_blood: str = None, pathologies: str = None,
        description_treatment: str = None, doctor_charge: str = None, day: int = None, month: int = None, year: int =
        None, date_treatment: date = None, mediator: Union[object, None] = None ) -> AbstractHistory: Create an
        instance of a MedicalHistory.
    """
    def create_agency(self, agency: AgencyFactory = AgencyFactory(),
                      medical_histories: List[Union[MedicalHistory, None]] = None) -> AbstractAgency:
        """
        Create an instance of a HealthAgency.

        Args:
            agency (AgencyFactory): The agency associated with the health agency.
            medical_histories (MedicalHistory): The medical histories of the agency.

        Returns:
            AbstractAgency: An instance of HealthAgency or its subclass.
        """
        if medical_histories is None:
            medical_histories = []
        return HealthAgency(username=str(agency.id_entity), agency=agency, medical_histories=medical_histories)

    def create_history(self, **data) -> AbstractHistory:
        """
        Create an instance of an EducationHistory.

        Args:
            data (dict): A dictionary containing the data for creating an EducationHistory.

        Returns:
            AbstractHistory: An instance of HealthHistory or its subclass.
        """
        return MedicalHistory(**data)
