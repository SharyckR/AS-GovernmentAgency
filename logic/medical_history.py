from datetime import date
from pydantic import BaseModel
from typing import Union, List
from logic.abstract_history import AbstractHistory


class MedicalHistory(AbstractHistory, BaseModel):
    """
     Class used to represent a Medical History
     Attributes:
            id_history (int): The identifier for the medical history.
            dni_person (int): DNI of the person to whom the history refers.
            type_blood (char): Attribute that is used to save the blood type of people's medical history.
            pathologies (string): Save the pathologies that people suffer from.
            date_treatment (datetime): Date of operation to be carried out.
            description_treatment (str): Attribute where it is about describing the treatment of the person.
            doctor_charge (str):Information about the doctor who will treat the person.

            mediator (object): Mediator for managing interactions.

        Methods:
            __str__(): Returns a string representation of a medical history.
            __eq__(other): Compares two objects medical history to check if they are equal.
    """
    id_history: int = 1
    dni_person: int = 123456789
    type_blood: str = "A+, B+, O+, AB+, A-, B-, O-, AB-"
    pathologies: Union[List[str], None] = None
    description_treatment: str = "Treatment description"
    doctor_charge: str = "Name doctor"
    day: int = 1
    month: int = 1
    year: int = 1999
    date_treatment: date = date(year, month, day)
    mediator: Union[object, None] = None

    def __init__(self, mediator=None, **data):
        super().__init__(**data)
        self.date_treatment = date(year=self.year, month=self.month, day=self.day)
        self.mediator = mediator

    def to_dict(self):
        return {
            str(self.dni_person): {
                "id_history": self.id_history,
                "type_blood": self.type_blood,
                "pathologies": self.pathologies if self.pathologies is not None else None,
                "description_treatment": self.description_treatment,
                "doctor_charge": self.doctor_charge,
                "date_treatment": str(self.date_treatment)
            }}

    def __eq__(self, other):
        """ Returns bool of equality of history objects.
        :returns: bool history
        :rtype: bool
        """
        if isinstance(other, MedicalHistory):
            return (self.id_history == other.id_history and self.dni_person == other.dni_person and
                    self.type_blood == other.type_blood and
                    self.pathologies == other.pathologies and
                    self.description_treatment == other.description_treatment and
                    self.doctor_charge == other.doctor_charge and self.day == other.day and
                    self.month == other.month and self.year == other.year and
                    self.date_treatment == other.date_treatment)
        return False

    def __str__(self):
        """ Returns str of medical history.
        :returns: string medical history
        :rtype: str
        """

        pathologies_str = str(self.pathologies) if self.pathologies is not None else "None"

        return ('ID History: {!r} DNI Person: {!r}, Type blood: {!r}, Pathologies: {!r}, Description treatment: {!r}, '
                'Doctor charge: {!r}, Date treatment: {!r} - {!r} - {!r}').format(
            self.id_history, self.dni_person, self.type_blood, pathologies_str, self.description_treatment,
            self.doctor_charge, self.year, self.month, self.day)


if __name__ == '__main__':
    # Prueba Medical History class

    medical_history1 = MedicalHistory(id_history=13, dni_person=1043638720, type_blood="O+", pathologies=None,
                                      description_treatment="Wound healing", doctor_charge="Kevin Rodriguez",
                                      day=5, month=10, year=2023)

    medical_history2 = MedicalHistory(id_history=14, dni_person=45761873, type_blood="A+", pathologies=["Hypertension"],
                                      description_treatment="Control", doctor_charge="Tomas Antonio",
                                      day=31, month=7, year=2023)

    medical_history1_str = medical_history1.__str__()
    print(f"Medical History 1 Information \n {medical_history1_str}")
    medical_history2_str = medical_history2.__str__()
    print(f"Case History 2 Information \n {medical_history2_str}")

    are_equal_medical_history = medical_history1.__eq__(medical_history2)
    print(f"Are equals ? \n {are_equal_medical_history} \n\n")

medical_history1 = MedicalHistory(
    id_history=13, dni_person=1043638720, type_blood="O+", pathologies=None, description_treatment="Wound healing",
    doctor_charge="Kevin Rodriguez", day=5, month=10, year=2023)
medical_history2 = MedicalHistory(
    id_history=14, dni_person=45761873, type_blood="A+", pathologies=["Hypertension"], description_treatment="Control",
    doctor_charge="Tomas Antonio", day=31, month=7, year=2023)
