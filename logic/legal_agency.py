from typing import List

from logic.agency_factory import *
from logic.case_history import *


class LegalAgency(AgencyFactory):
    """
    Represents a legal agency.
    Attributes:
        agency (object): The associated agency factory.
        case_histories (List): The legal histories.
    Methods:
        __str__(): Returns a formatted string with legal agency information.
        __eq__(other): Compares if two instances of LegalAgency are equal.
    """
    agency: AgencyFactory = AgencyFactory()
    agency.entity.subtype = "Legal Agency"
    case_histories: Union[List[CaseHistory], None] = []

    def __init__(self, username: Union[str, None] = None, agency: AgencyFactory = AgencyFactory(),
                 case_histories: List[CaseHistory] = None):
        super().__init__(agency=agency)
        self.username = username
        self.case_histories = case_histories or []

    def to_dict(self):
        case_histories = []
        for case_history in self.case_histories:
            case_histories.append(case_history.to_dict())
        return {f"{self.agency.id_entity}": {
            "agency": self.agency.to_dict(),
            "case_histories": case_histories
            }
        }

    def __str__(self):
        """ Returns str of legal agency.
        :returns: string legal agency
        :rtype: str
        """
        case_histories = ''
        for case_history in self.case_histories:
            case_histories += case_history.__str__() + ", "
        return 'Agency: {0}, Case Histories: {1}\n'.format(self.agency, case_histories)

    def __eq__(self, other):
        """
        Compares if two instances of LegalAgency are equal.

        Args:
            other (LegalAgency): The other instance to compare.

        Returns:
            bool: True if both instances are equal, otherwise False.
        """
        if isinstance(other, LegalAgency):
            return self.agency == other.agency and self.case_history == other.case_history
        return False


if __name__ == '__main__':
    legal1 = LegalAgency(agency=agency1, case_histories=[case_history1])
    legal2 = LegalAgency(agency=agency2, case_histories=[case_history2])
    legal2.case_histories.append(case_history1)
    print(f"Legal Agency 1 Information \n {legal1.__str__()}")
    print(f"Legal Agency 2 Information \n {legal2.__str__()}")

    are_equal_legal_agency = legal1.__eq__(legal2)
    print(f"Are equals ? \n {are_equal_legal_agency} \n\n")

legal1 = LegalAgency(agency=agency1, case_histories=[case_history1])
legal2 = LegalAgency(agency=agency2, case_histories=[case_history2])
