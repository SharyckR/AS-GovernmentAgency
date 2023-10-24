from typing import List
from logic.agency_factory import AgencyFactory, agency1, agency2
from logic.education_history import EducationHistory, edu_history1, edu_history2


class EducationalAgency(AgencyFactory):
    """
    Represents an educational agency.

    Attributes:
        agency (object): The associated agency.
        education_history (object): The education history.
        academic_achievements (List[str]): List of academic achievements.

    Methods:
        __str__(): Returns a formatted string with educational agency information.
        __eq__(other): Compares if two instances of EducationalAgency are equal.
    """
    agency: AgencyFactory = AgencyFactory()
    education_history: EducationHistory = EducationHistory()
    academic_achievements: List[str] = []

    def to_dict(self):
        return {f"{self.agency.id_entity}":  {
            "agency": self.agency.to_dict(),
            "education_history": self.education_history.to_dict(),
            "academic_achievements": self.academic_achievements
        }}

    def __str__(self):
        """
        Returns str of educational history.
        :returns: string educational history
        :rtype: str
        """
        return 'Agency: {0}, Education History: {1}, Academic achievements: {2}'.format(
            self.agency,
            self.education_history,
            self.academic_achievements
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
                self.education_history.__eq__(other.education_history) and
                self.academic_achievements == other.academic_achievements
            )
        return False


if __name__ == '__main__':
    educational1 = EducationalAgency(agency=agency1, education_history=edu_history1,
                                     academic_achievements=['Good Student, Best in maths'])
    educational2 = EducationalAgency(agency=agency2, education_history=edu_history2,
                                     academic_achievements=['Best in sports, More speed'])

    print(f"Educational Agency 1 Information \n {educational1}")
    print(f"Educational Agency 2 Information \n {educational2}")

    are_equal_medical_agency = educational1.__eq__(educational2)
    print(f"Are equals ? \n {are_equal_medical_agency} \n\n")

educational1 = EducationalAgency(agency=agency1, education_history=edu_history1,
                                 academic_achievements=['Good Students', 'Best in maths'])
educational2 = EducationalAgency(agency=agency2, education_history=edu_history2,
                                 academic_achievements=['Best in sports', 'More speed'])
