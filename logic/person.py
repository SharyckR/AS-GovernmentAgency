from logic.case_history import *
from logic.education_history import *
from logic.fine_history import *
from logic.medical_history import *
from logic.natural_entity import NaturalEntity
from logic.vehicle_history import *


class Person(NaturalEntity, BaseModel):
    """
     Class used to represent a Person
     Attributes:
            type_id_entity (str): Type id_entity.
            dni_person (int): DNI of person.
            type (str): Type id_entity of person.
            name (str): Name of person.
            last_name (str): Last name of person.
            phone (int): Phone of person.
            address (object): Address of person.
            education_history (object): Educational history of the person.
            fine_history (object): Fine history of the person.
            case_history (object): Case history of the person.
            medical_history (object): Medical history of the person.
            vehicle_history (object): Vehicle history of the person.
            mediator (object): Mediator for managing interactions.

        Methods:
            __str__(): Returns a string representation of a person.
            __eq__(other): Compares two objects person to check if they are equal.
    """
    type_id_entity: str = "C.C."
    dni_person: int = 123456789
    type: str = "C.C."
    name: str = "Name"
    last_name: str = "Last Name"
    phone: int = 12345678
    address: Address = Address()
    day: int = 1
    month: int = 1
    year: int = 1999
    birthday: date = date(year, month, day)
    education_history: EducationHistory = EducationHistory()
    fine_history: FineHistory = FineHistory()
    vehicle_history: VehicleHistory = VehicleHistory()
    case_history: CaseHistory = CaseHistory()
    medical_history: MedicalHistory = MedicalHistory()
    mediator: object = None

    def __init__(self, mediator=None, **data):
        super().__init__(**data)
        self.mediator = mediator
        self.username = str(self.dni_person)
        self.birthday: date = date(self.year, self.month, self.day)

    def to_dict(self):
        return {
            str(self.dni_person): {
                "type_id_entity": self.type_id_entity,
                "dni_person": self.dni_person,
                "type": self.type,
                "name": self.name,
                "last_name": self.last_name,
                "birthday": str(self.birthday),
                "phone": self.phone,
                "address": self.address.to_dict(),
                "education_history": self.education_history.to_dict(),
                "fine_history": self.fine_history.to_dict(),
                "vehicle_history": self.vehicle_history.to_dict(),
                "case_history": self.case_history.to_dict(),
                "medical_history": self.medical_history.to_dict()
            }
        }

    def __eq__(self, other):
        """ Returns bool of equality of person objects.
        :returns: bool person
        :rtype: bool
        """
        if isinstance(other, Person):
            return (self.type_id_entity == other.type_id_entity,
                    self.dni_person == other.dni_person and self.type == other.type and self.name == other.name and
                    self.last_name == other.last_name and self.phone == other.phone and
                    self.address == other.address and self.birthday == other.birthday and
                    self.education_history == other.education_history and
                    self.fine_history == other.fine_history and self.vehicle_history == other.vehicle_history and
                    self.case_history == other.case_history and self.medical_history == other.medical_history)
        return False

    def __str__(self):
        """ Returns str of person.
        :returns: string person
        :rtype: str
        """
        return ('Type ID Entity: {!r}, Dni Person: {!r}, Type DNI: {!r}, Full name: {!r} {!r}, Birthday: {!r}, '
                'Phone: {!r}, Address: {!r}, Education History: {!r}, Fine History: {!r}, Vehicle History: {!r}, '
                'Case History: {!r}, Medical History: {!r}'.
                format(self.type_id_entity, self.dni_person, self.type, self.name, self.last_name,
                       str(self.birthday), self.phone, self.address, self.education_history, self.fine_history,
                       self.vehicle_history, self.case_history, self.medical_history))


if __name__ == '__main__':
    # Prueba Person class

    person1 = Person(username="124230242", type_id_entity="C.C.", dni_person=124230242, type="C.C.",
                     name="María", last_name="Sarmiento", phone=313242323, address=address1, day=15, month=12,
                     year=2009)
    person2 = Person(username="45761873", type_id_entity="C.C", dni_person=45761873, type="C.E.",
                     name="Luis", last_name="Castro", phone=3214464925, address=address2, day=12, month=1, year=2002)

    person1_str = person1.__str__()
    print(f"Person 1 Information \n {person1_str}")
    person2_str = person2.__str__()
    print(f"Person 2 Information \n {person2_str}")

    are_equal_person = person1.__eq__(person2)
    print(f"Are equals ? \n {are_equal_person} \n\n")

person1 = Person(username="124230242", type_id_entity="C.C.", dni_person=124230242, type="C.C.",
                 name="María", last_name="Sarmiento", phone=313242323, address=address1, day=15, month=12, year=2009)
person2 = Person(username="45761873", type_id_entity="C.C", dni_person=45761873, type="C.E.",
                 name="Luis", last_name="Castro", phone=3214464925, address=address2, day=12, month=1, year=2002)
