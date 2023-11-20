from typing import List
from logic.agency_factory import AgencyFactory, agency1, agency2
from logic.education_history import EducationHistory, edu_history1, edu_history2


class EducationalAgency(AgencyFactory):
    """
    Represents an educational agency.
    Attributes:
        agency (AgencyFactory): The associated agency.
        education_histories (List[EducationHistory]): The education histories.
    Methods:
        to_dict(): Returns a dictionary representation of the educational agency.
        __str__(): Returns a formatted string with educational agency information.
        __eq__(other): Compares if two instances of EducationalAgency are equal.
    """
    agency: AgencyFactory = AgencyFactory()
    agency.entity.subtype = 'Educational Agency'
    education_histories: List[EducationHistory] = []

    def to_dict(self) -> dict:
        """
        Returns a dictionary representation of the educational agency.
        Returns:
            dict: Dictionary representation of the educational agency.
        """
        educational_histories = [edu_history.to_dict() for edu_history in self.education_histories]
        return {f"{self.agency.id_entity}": {
            "agency": self.agency.to_dict(), "education_histories": educational_histories
                }}

    def __str__(self) -> str:
        """
        Returns a formatted string with educational agency information.
        Returns:
            str: Formatted string with educational agency information.
        """
        educational_histories_str = ', '.join(str(edu_history) for edu_history in self.education_histories)
        return f'Agency: {self.agency}, Education Histories: {educational_histories_str}\n'

    def __eq__(self, other) -> bool:
        """
        Compares if two instances of EducationalAgency are equal.
        Args:
            other (EducationalAgency): The other instance to compare.
        Returns:
            bool: True if both instances are equal, otherwise False.
        """
        if isinstance(other, EducationalAgency):
            return self.agency.__eq__(other.agency) and self.education_histories.__eq__(other.education_histories)
        return False


if __name__ == '__main__':
    # Test Educational Agency class
    educational1 = EducationalAgency(agency=agency1, education_histories=[edu_history1])
    educational2 = EducationalAgency(agency=agency2, education_histories=[edu_history2])
    print(f"Educational Agency 1 Information \n {educational1}")
    print(f"Educational Agency 2 Information \n {educational2}")
    are_equal_educational_agency = educational1.__eq__(educational2)
    print(f"Are equals ? \n {are_equal_educational_agency} \n\n")

educational1 = EducationalAgency(agency=agency1, education_histories=[edu_history1])
educational2 = EducationalAgency(agency=agency2, education_histories=[edu_history2])
