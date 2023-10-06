from datetime import date
from pydantic import BaseModel


class MedicalHistory(BaseModel):
    """
     Class used to represent a Medical History

     Attributes:
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

    dni_person: int = 0
    type_blood: str = "A+, B+, O+, AB+, A-, B-, O-, AB-"
    pathologies: str = "Pathologies"
    description_treatment: str = "Treatment description"
    doctor_charge: str = "Name doctor"
    day: int = 1
    month: int = 1
    year: int = 1999
    date_treatment: date = date(year, month, day)
    mediator: object = None

    def __init__(self, mediator=None, **data):
        super().__init__(**data)
        self.mediator = mediator

    def __eq__(self, another_history):
        """ Returns bool of equality of history objects.
        :returns: bool history
        :rtype: bool
        """
        return another_history.dni_person == self.dni_person

    def __str__(self):
        """ Returns str of medical history.
        :returns: string medical history
        :rtype: str
        """
        return 'Dni: {0}, Type blood: {1}, Pathologies: {2}, Description treatment: {3}, Doctor charge: {4}, ' \
               'Date treatment: {5} - {6} - {7}'.format(self.dni_person, self.type_blood, self.pathologies,
                                                        self.description_treatment, self.doctor_charge, self.year,
                                                        self.month, self.day)
