from typing import List, Union

from logic.medical_history import MedicalHistory, medical_history1, medical_history2
from logic.agency_factory import AgencyFactory, agency1, agency2


class HealthAgency(AgencyFactory):
    """
    Represents a health agency.
    Attributes:
        agency (object): The associated agency factory.
        medical_histories (List): The medical histories.
    Methods:
        __str__(): Returns a formatted string with health agency information.
        __eq__(other): Compares if two instances of HealthAgency are equal.
    """
    agency: AgencyFactory = AgencyFactory()
    agency.entity.subtype = "Health Agency"
    medical_histories: List[Union[MedicalHistory, None]] = []

    def to_dict(self):
        medical_histories = []
        for medical_history in self.medical_histories:
            medical_histories.append(medical_history.to_dict())
        return {f"{self.agency.id_entity}": {
            "agency": self.agency.to_dict(),
            "medical_histories": medical_histories
        }}

    def __eq__(self, other):
        """
        Compares if two instances of HealthAgency are equal.
        Args:
            other (HealthAgency): The other instance to compare.
        Returns:
            bool: True if both instances are equal, otherwise False.
        """
        if isinstance(other, HealthAgency):
            return self.agency.__eq__(other.agency) and self.medical_histories.__eq__(other.medical_histories)
        else:
            return False

    def __str__(self):
        """
        Returns str of health agency information.
        :returns: string health agency information
        :rtype: str
        """
        return 'Agency information: {0}, Medical History: {1}\n'.format(self.agency.__str__(),
                                                                        self.medical_histories.__str__())


if __name__ == '__main__':
    health1 = HealthAgency(agency=agency1, medical_histories=[medical_history1])
    health2 = HealthAgency(agency=agency2, medical_histories=[medical_history2])

    print(f"Medical Agency 1 Information \n {health1}")
    print(f"Medical Agency 2 Information \n {health2}")

    are_equal_medical_agency = health1.__eq__(health2)
    print(f"Are equals ? \n {are_equal_medical_agency} \n\n")

health1 = HealthAgency(agency=agency1, medical_histories=[medical_history1])
health2 = HealthAgency(agency=agency2, medical_histories=[medical_history2])
