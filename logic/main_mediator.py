from logic.mediator import Mediator
from logic.person import person1, person2
from logic.fine_history import fine_history1, fine_history2
from logic.vehicle_history import vehicle_history1, vehicle_history2
from logic.education_history import edu_history1, edu_history2
from logic.medical_history import medical_history1, medical_history2
from logic.case_history import case_history1, case_history2


if __name__ == '__main__':
    # Prueba Mediator clas

    mediator = Mediator()

    mediator.add_person(person1)
    mediator.add_person(person2)
    print("\n")

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

    print("Education History for Person 1 and Person 2 \n")
    print(person1.education_history)
    print(person2.education_history)
    print("\n")

    print("Fine History for Person 1 and Person 2 \n")
    print(person1.fine_history)
    print(person2.fine_history)
    print("\n")

    print("Vehicle History for Person 1 and Person 2 \n")
    print(person1.vehicle_history)
    print(person2.vehicle_history)
    print("\n")

    print("Case History for Person 1 and Person 2 \n")
    print(person1.case_history)
    print(person2.case_history)
    print("\n")

    print("Medical History for Person 1 and Person 2 \n")
    print(person1.medical_history)
    print(person2.medical_history)
    print("\n")

    print("Search by person \n")
    found_person = mediator.get_person_by_dni(1043638720)
    if found_person:
        print(found_person.name)
        print("\n")
    else:
        print("Person not found\n")

    print("Education History search by person \n")
    found_education_history = mediator.get_education_history_by_dni(1043638720)
    if found_education_history:
        print(found_education_history.dni_person, found_education_history.education,
              found_education_history.name_institution, found_education_history.location,
              found_education_history.title_obtained, found_education_history.date_graduation)
        print("\n")
    else:
        print("Education history not found \n")

    print("Fine History search by person \n")
    found_fine_history = mediator.get_fine_history_by_dni(1043638720)
    if found_fine_history:
        print(found_fine_history.dni_person, found_fine_history.fine,
              found_fine_history.type_fine, found_fine_history.description_fine,
              found_fine_history.paid)
        print("\n")
    else:
        print("Fine history not found \n")

    print("Vehicle History search by person \n")
    found_vehicle_history = mediator.get_vehicle_history_by_dni(1043638720)
    if found_vehicle_history:
        print(found_vehicle_history.dni_person, found_vehicle_history.licence,
              found_vehicle_history.type_licence, found_vehicle_history.vehicle,
              found_vehicle_history.type_vehicle, found_vehicle_history.description_vehicle,
              found_vehicle_history.plate_vehicle)
        print("\n")
    else:
        print("Vehicle history not found \n")

    print("Case History search by person \n")
    found_case_history = mediator.get_case_history_by_dni(1043638720)
    if found_case_history:
        print(found_case_history.dni_person, found_case_history.case,
              found_case_history.arrested, found_case_history.description_case,
              found_case_history.jurisdiction, found_case_history.date_arrested)
        print("\n")
    else:
        print("Case history not found \n")

    print("Medical History search by person \n")
    found_medical_history = mediator.get_medical_history_by_dni(1043638720)
    if found_medical_history:
        print(found_medical_history.dni_person, found_medical_history.type_blood,
              found_medical_history.pathologies, found_medical_history.description_treatment,
              found_medical_history.doctor_charge, found_medical_history.date_treatment)
        print("\n")
    else:
        print("Medical history not found \n")
