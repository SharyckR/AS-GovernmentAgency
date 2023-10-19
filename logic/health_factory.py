from datetime import date
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
                       description_treatment: str = None, doctor_charge: str = None, day: int = None,
                       month: int = None, year: int = None, date_treatment: date = None, mediator: object = None
                       ) -> AbstractHistory:
            Create an instance of a MedicalHistory.
    """
    def create_agency(self, agency: AgencyFactory = None, medical_history: MedicalHistory = None) -> AbstractAgency:
        """
        Create an instance of a HealthAgency.

        Args:
            agency (AgencyFactory): The agency associated with the health agency.
            medical_history (MedicalHistory): The medical history of the agency.

        Returns:
            AbstractAgency: An instance of HealthAgency or its subclass.
        """
        return HealthAgency(agency=agency, medical_history=medical_history)

    def create_history(self, dni_person: int = None, type_blood: str = None, pathologies: str = None,
                       description_treatment: str = None, doctor_charge: str = None, day: int = None,
                       month: int = None, year: int = None, date_treatment: date = None, mediator: object = None
                       ) -> AbstractHistory:
        """
        Create an instance of a MedicalHistory.

        Args:
            dni_person (int): The DNI of the person with the medical history.
            type_blood (str): Blood type information.
            pathologies (str): Pathologies information.
            description_treatment (str): Description of treatment.
            doctor_charge (str): Doctor's charge.
            day (int): Day of treatment.
            month (int): Month of treatment.
            year (int): Year of treatment.
            date_treatment (date): Date of treatment.
            mediator (object): Mediator object.

        Returns:
            AbstractHistory: An instance of MedicalHistory or its subclass.
        """
        return MedicalHistory(dni_person=dni_person, type_blood=type_blood, pathologies=pathologies,
                              description_treatment=description_treatment, doctor_charge=doctor_charge,
                              day=day, month=month, year=year, date=date_treatment, mediator=mediator)
