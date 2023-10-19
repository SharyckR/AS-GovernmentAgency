from logic.medical_history import MedicalHistory, medical_history1, medical_history2
from logic.agency_factory import AgencyFactory, agency1, agency2


class HealthAgency(AgencyFactory):
    """
    Represents a health agency.

    Attributes:
        agency (object): The associated agency factory.
        medical_history (object): The medical history.

    Methods:
        __str__(): Returns a formatted string with health agency information.
        __eq__(other): Compares if two instances of HealthAgency are equal.
    """
    agency: AgencyFactory = AgencyFactory()
    medical_history: MedicalHistory = MedicalHistory()

    def to_dict(self):
        return {
            "Agency": self.agency.to_dict(),
            "Medical History": self.medical_history.to_dict()
               }

    def __eq__(self, other):
        """
        Compares if two instances of HealthAgency are equal.

        Args:
            other (HealthAgency): The other instance to compare.

        Returns:
            bool: True if both instances are equal, otherwise False.
        """
        if isinstance(other, HealthAgency):
            return self.agency.__eq__(other.agency) and self.medical_history.__eq__(other.medical_history)
        else:
            return False

    def __str__(self):
        """
        Returns str of health agency information.
        :returns: string health agency information
        :rtype: str
        """
        return 'Agency information: {0}, Medical History: {1}'.format(self.agency.__str__(),
                                                                      self.medical_history.__str__())


if __name__ == '__main__':
    health1 = HealthAgency(agency=agency1, medical_history=medical_history1)
    health2 = HealthAgency(agency=agency2, medical_history=medical_history2)

    print(f"Medical Agency 1 Information \n {health1}")
    print(f"Medical Agency 2 Information \n {health2}")

    are_equal_medical_agency = health1.__eq__(health2)
    print(f"Are equals ? \n {are_equal_medical_agency} \n\n")

health1 = HealthAgency(agency=agency1, medical_history=medical_history1)
health2 = HealthAgency(agency=agency2, medical_history=medical_history2)
