from typing import List, Union
from logic.agency_factory import AgencyFactory, agency1, agency2
from logic.education_history import EducationHistory, edu_history1, edu_history2


class EducationalAgency(AgencyFactory):
    """
    Represents an educational agency.
    Attributes:
        agency (object): The associated agency.
        education_histories (List): The education histories.
    Methods:
        __str__(): Returns a formatted string with educational agency information.
        __eq__(other): Compares if two instances of EducationalAgency are equal.
    """
    agency: AgencyFactory = AgencyFactory()
    agency.entity.subtype = 'Educational Agency'
    education_histories: Union[List[EducationHistory], None] = []

    def __init__(self, username: Union[str, None] = None,  agency: AgencyFactory = AgencyFactory(),
                 education_histories: List[EducationHistory] = None):
        super().__init__(agency=agency)
        self.username = username
        self.education_histories = education_histories or []

    def to_dict(self):
        educational_histories = []
        for educational_history in self.education_histories:
            educational_histories.append(educational_history.to_dict())
        return {f"{self.agency.id_entity}": {
            "agency": self.agency.to_dict(),
            "education_histories": educational_histories
        }
        }

    def __str__(self):
        """
        Returns str of educational history.
        :returns: string educational history
        :rtype: str
        """
        educational_histories = ''
        for educational_history in self.education_histories:
            educational_histories += educational_history.__str__() + ", "
        return 'Agency: {0}, Education History: {1}\n'.format(
            self.agency,
            educational_histories,
        )

    def __eq__(self, other):
        """
        Compares if two instances of EducationalAgency are equal.
        Args:
            other (EducationalAgency): The other instance to compare.
        Returns:
            bool: True if both instances are equal, otherwise False.
        """
        if isinstance(other, EducationalAgency):
            return (
                    self.agency.__eq__(other.agency) and
                    self.education_histories.__eq__(other.education_histories)
            )
        return False


if __name__ == '__main__':
    educational1 = EducationalAgency(agency=agency1, education_histories=[edu_history1])
    educational2 = EducationalAgency(agency=agency2, education_histories=[edu_history2])

    print(f"Educational Agency 1 Information \n {educational1}")
    print(f"Educational Agency 2 Information \n {educational2}")

    are_equal_medical_agency = educational1.__eq__(educational2)
    print(f"Are equals ? \n {are_equal_medical_agency} \n\n")

educational1 = EducationalAgency(agency=agency1, education_histories=[edu_history1])
educational2 = EducationalAgency(agency=agency2, education_histories=[edu_history2])
