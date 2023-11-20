from typing import List, Union
from logic.abstract_factory import AbstractFactory
from logic.abstract_agency import AbstractAgency
from logic.abstract_history import AbstractHistory
from logic.agency_factory import AgencyFactory
from logic.case_history import CaseHistory
from logic.legal_agency import LegalAgency


class LegalFactory(AbstractFactory):
    """
    Concrete factory for creating legal agency and history objects.
    Methods:
        create_agency(agency: AgencyFactory = AgencyFactory(),
                      case_histories: List[Union[CaseHistory, None]] = None) -> AbstractAgency:
            Create an instance of a LegalAgency.
        create_history(**data) -> AbstractHistory:
            Create an instance of a CaseHistory.
    """
    def create_agency(self, agency: AgencyFactory = AgencyFactory(),
                      case_histories: List[Union[CaseHistory, None]] = None) -> AbstractAgency:
        """
        Create an instance of a LegalAgency.
        Args:
            agency (AgencyFactory): The agency associated with the legal agency.
            case_histories (List[Union[CaseHistory, None]]): The legal histories of the agency.
        Returns:
            AbstractAgency: An instance of LegalAgency or its subclass.
        """
        if case_histories is None:
            case_histories = []
        return LegalAgency(username=str(agency.id_entity), agency=agency, case_histories=case_histories)

    def create_history(self, **data) -> AbstractHistory:
        """
        Create an instance of a CaseHistory.
        Args:
            data (dict): A dictionary containing the data for creating a CaseHistory.
        Returns:
            AbstractHistory: An instance of CaseHistory or its subclass.
        """
        return CaseHistory(**data)
