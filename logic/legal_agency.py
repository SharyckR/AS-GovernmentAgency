from pydantic import BaseModel
from logic.agency_factory import AgencyFactory, agency1, agency2
from logic.case_history import CaseHistory, case_history1, case_history2


class LegalAgency(AgencyFactory, BaseModel):
    """
    Represents a legal agency.

    Attributes:
        agency (object): The associated agency factory.
        legal_history (object): The legal history.

    Methods:
        __str__(): Returns a formatted string with legal agency information.
        __eq__(other): Compares if two instances of LegalAgency are equal.
    """
    agency: AgencyFactory = AgencyFactory()
    legal_history: CaseHistory = CaseHistory()

    def to_dict(self):
        return {
            "Agency": self.agency.to_dict(),
            "Case History": self.legal_history.to_dict()
        }

    def __str__(self):
        """ Returns str of legal agency.
        :returns: string legal agency
        :rtype: str
        """
        return '(Agency: {0}, Case History: {1})'.format(self.agency.__str__(), self.legal_history.__str__())

    def __eq__(self, other):
        """
        Compares if two instances of LegalAgency are equal.

        Args:
            other (LegalAgency): The other instance to compare.

        Returns:
            bool: True if both instances are equal, otherwise False.
        """
        if isinstance(other, LegalAgency):
            return self.agency.__eq__(other.agency) and self.legal_history.__eq__(other.legal_history)


if __name__ == '__main__':
    legal1 = LegalAgency(agency=agency1, legal_history=case_history1)
    legal2 = LegalAgency(agency=agency2, legal_history=case_history2)

    print(f"Legal Agency 1 Information \n {legal1.__str__()}")
    print(f"Legal Agency 2 Information \n {legal2.__str__()}")

    are_equal_legal_agency = legal1.__eq__(legal2)
    print(f"Are equals ? \n {are_equal_legal_agency} \n\n")

legal1 = LegalAgency(agency=agency1, legal_history=case_history1)
legal2 = LegalAgency(agency=agency2, legal_history=case_history1)
