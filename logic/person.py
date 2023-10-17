<<<<<<< HEAD

=======
>>>>>>> a92ca7333fcb1be9ac5737376a81e1802a1c3ed0
from logic.case_history import *
from logic.education_history import *
from logic.fine_history import *
from logic.medical_history import *
from logic.vehicle_history import *
from logic.address import *
from logic.natural_entity import NaturalEntity
from pydantic import BaseModel


class Person(NaturalEntity, BaseModel):
    """
     Class used to represent a Person

     Attributes:
            id_entity (int): id_entity of person ( used in the database ).
            type_id_entity (str): Type id_entity.
            dni (int): DNI of person.
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
<<<<<<< HEAD
    id_entity: int = 123456789
    type_id_entity: str = "C.C."
    dni: int = 123456789
    type: str = "C.C."
    name: str = "Name"
    last_name: str = "Last Name"
    phone: int = 12345678
    address: Address = Address()
    education_history: EducationHistory = EducationHistory()
    fine_history: FineHistory = FineHistory()
    vehicle_history: VehicleHistory = VehicleHistory()
    case_history: CaseHistory = CaseHistory()
    medical_history: MedicalHistory = MedicalHistory()
=======
    id_entity: int = 00000000
    type_id_entity: str = "Type id_entity"
    dni: int = 123456789
    type: str = "Type dni person"
    name: str = "Name"
    last_name: str = "LastName"
    phone: int = 0
    address: object = Address
    education_history: object = EducationHistory()
    fine_history: object = FineHistory()
    vehicle_history: object = VehicleHistory()
    case_history: object = CaseHistory()
    medical_history: object = MedicalHistory()
>>>>>>> a92ca7333fcb1be9ac5737376a81e1802a1c3ed0
    mediator: object = None

    def __init__(self, mediator=None, **data):
        super().__init__(**data)
        self.mediator = mediator

    def to_dict(self):
        return {
            "DNI Person": self.dni,
            "Type DNI": self.type,
            "Name": self.name,
            "Last Name": self.last_name,
            "Phone": self.phone,
            "Address": self.address.to_dict(),
            "Education History": self.education_history.to_dict(),
            "Fine History": self.fine_history.to_dict(),
            "Vehicle History": self.vehicle_history.to_dict(),
            "Case History": self.case_history.to_dict(),
            "Medical History": self.medical_history.to_dict()
        }

    def __eq__(self, other):
        """ Returns bool of equality of person objects.
        :returns: bool person
        :rtype: bool
        """
        if isinstance(other, Person):
            return (self.id_entity == other.id_entity, self.type_id_entity == other.type_id_entity,
                    self.dni == other.dni and self.type == other.type and self.name == other.name and
                    self.last_name == other.last_name and self.phone == other.phone and
                    self.address == other.address and self.education_history == other.education_history and
                    self.fine_history == other.fine_history and self.vehicle_history == other.vehicle_history and
                    self.case_history == other.case_history and self.medical_history == other.medical_history)
        return False

    def __str__(self):
        """ Returns str of person.
        :returns: string person
        :rtype: str
        """
        return 'ID entity: {0}, Type ID Entity: {1}, Dni Person: {2}, Type DNI: {3}, Full name: {4} {5}, Phone: {6}, ' \
               'Address: {7}, Education History: {8}, Fine History: {9}, Vehicle History: {10}, Case History: {11}, ' \
               'Medical History: {12}'.\
            format(self.id_entity, self.type_id_entity, self.dni, self.type, self.name, self.last_name, self.phone,
                   self.address, self.education_history, self.fine_history, self.vehicle_history, self.case_history,
                   self.medical_history)


if __name__ == '__main__':
    # Prueba Person class

    person1 = Person(id_entity=5120167, type_id_entity="C.C", dni=1043638720, name="Julio", type="C.C.",
                     last_name="Rodriguez", phone=3154528309, address=address1)
    person2 = Person(id_entity=1247913, type_id_entity="C.C", dni=45761873, type="C.E.", name="Luis",
                     last_name="Castro", phone=3214464925, address=address2)

    person1_str = person1.__str__()
    print(f"Person 1 Information \n {person1_str}")
    person2_str = person2.__str__()
    print(f"Person 2 Information \n {person2_str}")

    are_equal_person = person1.__eq__(person2)
    print(f"Are equals ? \n {are_equal_person} \n\n")

<<<<<<< HEAD
person1 = Person(id_entity=5120167, type_id_entity="C.C", dni=1043638721, type="C.C.", name="Julio",
=======
person1 = Person(id_entity=5120167, type_id_entity="C.C", dni=1043638720, type="C.C.", name="Julio",
>>>>>>> a92ca7333fcb1be9ac5737376a81e1802a1c3ed0
                 last_name="Rodriguez", phone=3154528309, address=address1)
person2 = Person(id_entity=1247913, type_id_entity="C.C", dni=45761873, type="C.E.", name="Luis", last_name="Castro",
                 phone=3214464925, address=address2)
