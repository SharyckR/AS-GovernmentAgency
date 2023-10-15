from controller.mediator import Mediator
from logic.person import *
from logic.fine_history import *
from logic.vehicle_history import *
from logic.education_history import *
from logic.medical_history import *
from logic.case_history import *


if __name__ == '__main__':
    # Prueba Mediator clas

    mediator = Mediator()

    mediator.add_education_history(edu_history1)
    mediator.add_education_history(edu_history2)
    print("\n")

    mediator.add_fine_history(fine_history1)
    mediator.add_fine_history(fine_history2)
    print("\n")

    mediator.add_vehicle_history(vehicle_history1)
    mediator.add_vehicle_history(vehicle_history2)
    print("\n")

    mediator.add_case_history(case_history1)
    mediator.add_case_history(case_history2)
    print("\n")

    mediator.add_medical_history(medical_history1)
    mediator.add_medical_history(medical_history2)
    print("\n")

    mediator.add_person(person1)
    mediator.add_person(person2)
    print("\n")

    mediator.link_education_history_to_person(edu_history1, person1)
    mediator.link_education_history_to_person(edu_history2, person2)
    print("\n")

    mediator.link_fine_history_to_person(fine_history1, person1)
    mediator.link_fine_history_to_person(fine_history2, person2)
    print("\n")

    mediator.link_vehicle_history_to_person(vehicle_history1, person1)
    mediator.link_vehicle_history_to_person(vehicle_history2, person2)
    print("\n")

    mediator.link_case_history_to_person(case_history1, person1)
    mediator.link_case_history_to_person(case_history2, person2)
    print("\n")

    mediator.link_medical_history_to_person(medical_history1, person1)
    mediator.link_medical_history_to_person(medical_history2, person2)
    print("\n")

    print("Search by person")
    found_person1 = mediator.get_person_by_dni(1043638720)
    found_person2 = mediator.get_person_by_dni(45761873)
    print(found_person1)
    print("\n")

    print("Education History search by person")
    found_education_history1 = mediator.get_education_history_by_dni(1043638720)
    found_education_history2 = mediator.get_education_history_by_dni(45761873)
    print(found_education_history1)
    print("\n")

    print("Fine History search by person \n")
    found_fine_history1 = mediator.get_fine_history_by_dni(1043638720)
    found_fine_history2 = mediator.get_fine_history_by_dni(45761873)
    print(found_fine_history2)
    print("\n")

    print("Vehicle History search by person \n")
    found_vehicle_history1 = mediator.get_vehicle_history_by_dni(1043638720)
    found_vehicle_history2 = mediator.get_vehicle_history_by_dni(5841254)
    print(found_vehicle_history2)
    print("\n")

    print("Case History search by person \n")
    found_case_history1 = mediator.get_case_history_by_dni(1043638720)
    found_case_history2 = mediator.get_case_history_by_dni(45761873)
    print(found_case_history1)
    print("\n")

    print("Medical History search by person \n")
    found_medical_history1 = mediator.get_medical_history_by_dni(1043638720)
    found_medical_history2 = mediator.get_medical_history_by_dni(45761873)
    print(found_medical_history1)
    print("\n")
