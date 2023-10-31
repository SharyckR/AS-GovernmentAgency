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
                      medical_history: MedicalHistory = MedicalHistory()) -> AbstractAgency:
        """
        Create an instance of a HealthAgency.

        Args:
            agency (AgencyFactory): The agency associated with the health agency.
            medical_history (MedicalHistory): The medical history of the agency.

        Returns:
            AbstractAgency: An instance of HealthAgency or its subclass.
        """
        return HealthAgency(username=str(agency.id_entity), agency=agency, medical_history=medical_history)

    def create_history(self, **data) -> AbstractHistory:
        """
        Create an instance of an EducationHistory.

        Args:
            data (dict): A dictionary containing the data for creating an EducationHistory.

        Returns:
            AbstractHistory: An instance of HealthHistory or its subclass.
        """
        return MedicalHistory(**data)
