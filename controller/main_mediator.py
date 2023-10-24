from controller.mediator import *
from logic.person import *
from logic.fine_history import *
from logic.vehicle_history import *
from logic.education_history import *
from logic.medical_history import *
from logic.case_history import *


if __name__ == '__main__':

    mediator = Mediator()

    mediator.add_person(person1)
    # mediator.add_person(person2)
    print("\n")

    mediator.link_education_history_to_person(person1.dni_person, edu_history1)
    # mediator.link_education_history_to_person(person2.dni, edu_history2)
    print("\n")

    mediator.link_fine_history_to_person(person1.dni_person, fine_history1)
    # mediator.link_fine_history_to_person(person2.dni, fine_history2)
    print("\n")

    mediator.link_vehicle_history_to_person(person1.dni_person, vehicle_history1)
    # mediator.link_vehicle_history_to_person(person2.dni, vehicle_history2)
    print("\n")

    mediator.link_case_history_to_person(person1.dni_person, case_history1)
    # mediator.link_case_history_to_person(person2.dni, case_history2)
    print("\n")

    mediator.link_medical_history_to_person(person1.dni_person, medical_history1)
    # mediator.link_medical_history_to_person(person2.dni, medical_history2)
    print("\n")

    print(get_person_info(person1.dni_person))
    print("\n")

    print(get_educational_history(person1.dni_person))
    print("\n")

    print(get_fine_history(person1.dni_person))
    print("\n")

    print(get_vehicle_history(person1.dni_person))
    print("\n")

    print(get_case_history(person1.dni_person))
    print("\n")

    print(get_medical_history(person1.dni_person))
    print("\n")
