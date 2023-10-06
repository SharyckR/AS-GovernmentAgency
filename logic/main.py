from datetime import date
from logic.case_history import CaseHistory
from logic.fine_history import FineHistory
from logic.medical_history import MedicalHistory
from logic.person import Person
from logic.address import Address
from logic.agency import Agency
from logic.education_history import EducationHistory
from logic.mediator import Mediator
from logic.vehicle_history import VehicleHistory

if __name__ == '__main__':
    # Prueba Address class

    address1 = Address(street='The cross', number=10, apartment=None, postal_code=1010, locality='Aqueous',
                       department='Cundinamarca', country='Colombia')
    address2 = Address(street='The cross', number=10, apartment=None, postal_code=1010, locality='Aqueous',
                       department='Cundinamarca', country='Colombia')

    address_str = address1.__str__()
    # print(address_str)

    are_equal_address = address1.__eq__(address2)
    # print(are_equal_address)

    # Prueba Person class

    person1 = Person(id_person=5120167, type_id="C.C", dni=1043638720, name="Julio", last_name="Rodriguez",
                     phone=3154528309, address=address1)
    person2 = Person(id_person=1247913, type_id="C.C", dni=45761873, name="Luis", last_name="Castro",
                     phone=3214464925, address="Colombia")

    person_str = person1.__str__()
    # print(person_str)

    are_equal_person = person1.__eq__(person2)
    # print(are_equal_person)

    # Prueba Agency class

    agency1 = Agency(id_agency=965816, nit=52173, business_name="Tiserium", contact="31459750", address=address2,
                     day=5, month=10, year=2023)

    agency2 = Agency(id_agency=965816, nit=52173, business_name="Tiserium", contact="31459750", address=address2,
                     day=5, month=10, year=2023)

    agency_str = agency1.__str__()
    # print(agency_str)

    are_equal_agency = agency1.__eq__(agency2)
    # print(are_equal_agency)

    # Prueba Educational History class

    edu_history1 = EducationHistory(dni_person=1043638720, education="Secondary", name_institution="Collage",
                                    location=address2, title_obtained="Graduated", day=13, month=10, year=2020)

    edu_history2 = EducationHistory(dni_person=45761873, education=None, name_institution=None,
                                    location=None, title_obtained=None, day=None, month=None, year=None)

    edu_history_str = edu_history2.__str__()
    # print(edu_history_str)

    are_equal_edu_history = edu_history1.__eq__(edu_history2)
    # print(are_equal_edu_history)

    # Prueba Fine History class

    fine_history1 = FineHistory(dni_person=1043638720, fine="Yes", type_fine="Fine for high speed",
                                description_fine="The person was going more than 100k/h", paid="No")

    fine_history2 = FineHistory(dni_person=45761873, fine="No", type_fine=None, description_fine=None, paid=None)

    fine_history_str = fine_history1.__str__()
    # print(fine_history_str)

    are_equal_fine_history = fine_history1.__eq__(fine_history2)
    # print(are_equal_fine_history)

    # Prueba Vehicle History class

    vehicle_history1 = VehicleHistory(dni_person=1043638720, licence="Yes", type_licence="A2", vehicle="Yes",
                                      type_vehicle="Car", description_vehicle="Mazda2", plate_vehicle="BJU-521")

    vehicle_history2 = VehicleHistory(dni_person=45761873, licence="No", type_licence=None, vehicle="Yes",
                                      type_vehicle="Motorcycle", description_vehicle="Honda", plate_vehicle="PLO-154")

    vehicle_history_str = vehicle_history1.__str__()
    print(vehicle_history_str)

    are_equal_vehicle_history = vehicle_history1.__eq__(vehicle_history2)
    print(are_equal_vehicle_history)

    # Prueba Case History class

    case_history1 = CaseHistory(dni_person=1043638720, case="Heist", arrested="Yes",
                                description_case="Stole a necklace", jurisdiction="Disciplinary", day=15, year=2021,
                                month=5)

    case_history2 = CaseHistory(dni_person=45761873, case="Public disturbance", arrested="No", description_case=None,
                                jurisdiction=None, day=None, year=None, month=None)

    case_history_str = case_history1.__str__()
    print(case_history_str)

    are_equal_case_history = case_history1.__eq__(case_history2)
    print(are_equal_case_history)

    # Prueba Medical History class

    medical_history1 = MedicalHistory(dni_person=1043638720, type_blood="O+", pathologies="None",
                                      description_treatment="Wound healing", doctor_charge="Kevin Rodriguez",
                                      day=5, month=10, year=2023, date_treatment=date(2023, 10, 5))

    medical_history2 = MedicalHistory(dni_person=45761873, type_blood="A+", pathologies="Hypertension",
                                      description_treatment="Control", doctor_charge="Tomas Antonio",
                                      day=31, month=7, year=2023, date_treatment=date(2023, 7, 31))

    medical_history_str = medical_history1.__str__()
    print(medical_history_str)

    are_equal_medical_history = medical_history1.__eq__(medical_history2)
    print(are_equal_medical_history)

    # Prueba Mediator clas

    mediator = Mediator()

    mediator.add_person(person1)
    mediator.add_person(person2)

    # mediator.add_education_history(edu_history1)
    # mediator.add_education_history(edu_history2)

    # mediator.add_fine_history(fine_history1)
    # mediator.add_fine_history(fine_history2)

    mediator.add_vehicle_history(vehicle_history1)
    mediator.add_vehicle_history(vehicle_history2)

    mediator.add_case_history(case_history1)
    mediator.add_case_history(case_history2)

    mediator.add_medical_history(medical_history1)
    mediator.add_medical_history(medical_history2)

    # mediator.link_education_history_to_person(edu_history1, person1)
    # mediator.link_education_history_to_person(edu_history2, person2)

    # mediator.link_fine_history_to_person(fine_history1, person1)
    # mediator.link_fine_history_to_person(fine_history2, person2)

    mediator.link_vehicle_history_to_person(vehicle_history1, person1)
    mediator.link_vehicle_history_to_person(vehicle_history2, person2)

    mediator.link_case_history_to_person(case_history1, person1)
    mediator.link_case_history_to_person(case_history2, person2)

    mediator.link_medical_history_to_person(medical_history1, person1)
    mediator.link_medical_history_to_person(medical_history2, person2)

    # print(person1.education_history)
    # print(person2.education_history)

    # print(person1.fine_history)
    # print(person2.fine_history)

    print(person1.vehicle_history)
    print(person2.vehicle_history)

    print(person1.case_history)
    print(person2.case_history)

    print(person1.medical_history)
    print(person2.medical_history)

    """ found_person = mediator.get_person_by_dni(1043638720)
    if found_person:
        print(found_person.name)
    else:
        print("Person not found") """

    """ found_education_history = mediator.get_education_history_by_dni(1043638720)
    if found_education_history:
        print(found_education_history.dni_person, found_education_history.education,
              found_education_history.name_institution, found_education_history.location,
              found_education_history.title_obtained, found_education_history.date_graduation)
    else:
        print("Education history not found") """

    """ found_fine_history = mediator.get_fine_history_by_dni(1043638720)
    if found_fine_history:
        print(found_fine_history.dni_person, found_fine_history.fine,
              found_fine_history.type_fine, found_fine_history.description_fine,
              found_fine_history.paid)
    else:
        print("Fine history not found") """

    found_vehicle_history = mediator.get_vehicle_history_by_dni(1043638720)
    if found_vehicle_history:
        print(found_vehicle_history.dni_person, found_vehicle_history.licence,
              found_vehicle_history.type_licence, found_vehicle_history.vehicle,
              found_vehicle_history.type_vehicle, found_vehicle_history.description_vehicle,
              found_vehicle_history.plate_vehicle)
    else:
        print("Vehicle history not found")

    found_case_history = mediator.get_case_history_by_dni(1043638720)
    if found_case_history:
        print(found_case_history.dni_person, found_case_history.case,
              found_case_history.arrested, found_case_history.description_case,
              found_case_history.jurisdiction, found_case_history.date_arrested)
    else:
        print("Case history not found")

    found_medical_history = mediator.get_medical_history_by_dni(1043638720)
    if found_medical_history:
        print(found_medical_history.dni_person, found_medical_history.type_blood,
              found_medical_history.pathologies, found_medical_history.description_treatment,
              found_medical_history.doctor_charge, found_medical_history.date_treatment)
    else:
        print("Medical history not found")
