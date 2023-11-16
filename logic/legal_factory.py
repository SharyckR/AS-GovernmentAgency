from typing import List, Union

from logic.abstract_factory import AbstractFactory
from logic.abstract_agency import AbstractAgency
from logic.abstract_history import AbstractHistory
from logic.agency_factory import AgencyFactory
from logic.case_history import CaseHistory
from logic.legal_agency import LegalAgency


class LegalFactory(AbstractFactory):
    """
    Concrete factory for creating legal agency and history objects. Methods: create_agency(agency: AgencyFactory =
    AgencyFactory(), legal_history: CaseHistory = CaseHistory()) -> AbstractAgency: Create an instance of a LegalAgency.

        create_history(id_history: int = 1, dni_person: int = 123456789, case: str = "Name case", arrested: str =
        "Yes or No", description_case: Union[str, None] = "Description of case", jurisdiction: Union[str,
        None] = "Jurisdiction of the case", day: int = 1, month: int = 1,
        year: int = 1999, date_arrested: date = date(year, month, day), mediator: Union[object, None] = None) ->
        AbstractHistory: Create an instance of a CaseHistory.
    """
    def create_agency(self, agency: AgencyFactory = AgencyFactory(),
                      case_histories: List[Union[CaseHistory, None]] = None) -> AbstractAgency:
        """
        Create an instance of a LegalAgency.
        Args:
            agency (AgencyFactory): The agency associated with the legal agency.
            case_histories (CaseHistory): The legal histories of the agency.
        Returns:
            AbstractAgency: An instance of LegalAgency or its subclass.
        """
        return LegalAgency(username=str(agency.id_entity), agency=agency, case_histories=case_histories)

    def create_history(self, **data) -> AbstractHistory:
        """
        Create an instance of an EducationHistory.
        Args:
            data (dict): A dictionary containing the data for creating an LegalHistory.
        Returns:
            AbstractHistory: An instance of EducationHistory or its subclass.
        """
        return CaseHistory(**data)
