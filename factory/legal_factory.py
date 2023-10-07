from datetime import date
from typing import Optional

from factory.abstract_factory import AbstractFactory
from logic.abstract_agency import AbstractAgency
from logic.abstract_history import AbstractHistory
from logic.agency import Agency
from logic.case_history import CaseHistory
from logic.legal_agency import LegalAgency


class LegalFactory(AbstractFactory):
    """
    Concrete factory for creating legal agency and history objects.

    Attributes:
        None

    Methods:
        create_agency(agency: Agency = None, legal_history: CaseHistory = None) -> AbstractAgency:
            Create an instance of a LegalAgency.

        create_history(dni_person: int = None, case: str = None, arrested: str = None,
                       description_case: Optional[str] = None, jurisdiction: Optional[str] = None,
                       day: Optional[int] = None, month: Optional[int] = None, year: Optional[int] = None,
                       date_arrested: Optional[date] = None, mediator: object = None) -> AbstractHistory:
            Create an instance of a CaseHistory.
    """
    def create_agency(self, agency: Agency = None, legal_history: CaseHistory = None) -> AbstractAgency:
        """
        Create an instance of a LegalAgency.

        Args:
            agency (Agency): The agency associated with the legal agency.
            legal_history (CaseHistory): The legal history of the agency.

        Returns:
            AbstractAgency: An instance of LegalAgency or its subclass.
        """
        return LegalAgency(agency=agency, legal_history=legal_history)

    def create_history(self, dni_person: int = None, case: str = None, arrested: str = None,
                       description_case: Optional[str] = None, jurisdiction: Optional[str] = None,
                       day: Optional[int] = None, month: Optional[int] = None, year: Optional[int] = None,
                       date_arrested: Optional[date] = None, mediator: object = None) -> AbstractHistory:
        """
        Create an instance of a CaseHistory.

        Args:
            dni_person (int): The DNI of the person with the legal history.
            case (str): Case information.
            arrested (str): Arrested information.
            description_case (str): Description of the case.
            jurisdiction (str): Jurisdiction information.
            day (int): Day of arrest.
            month (int): Month of arrest.
            year (int): Year of arrest.
            date_arrested (date): Date of arrest.
            mediator (object): Mediator object.

        Returns:
            AbstractHistory: An instance of CaseHistory or its subclass.
        """
        return CaseHistory(dni_person=dni_person, case=case, arrested=arrested, description_case=description_case,
                           jurisdiction=jurisdiction, day=day, month=month, year=year, date_arrested=date_arrested,
                           mediator=mediator)
