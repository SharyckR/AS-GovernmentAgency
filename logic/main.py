from datetime import date

from logic.fine_history import FineHistory
from logic.person import Person
from logic.address import Address
from logic.agency import Agency
from logic.education_history import EducationHistory
from logic.mediator import Mediator


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
                                    location=address2, title_obtained="Graduated", day=13, month=10, year=2020,
                                    date_graduation=date(2023, 10, 13))

    edu_history2 = EducationHistory(dni_person=45761873, education="Technical", name_institution="SENA",
                                    location=address1, title_obtained="Graduated", day=25, month=5, year=2012,
                                    date_graduation=date(2012, 5, 25))

    edu_history_str = edu_history1.__str__()
    # print(edu_history_str)

    are_equal_edu_history = edu_history1.__eq__(edu_history2)
    # print(are_equal_edu_history)

    # Prueba Fine History class

    fine_history1 = FineHistory(dni_person=1043638720, fine="Yes", type_fine="Fine for high speed",
                                description_fine="The person was going more than 100k/h", paid="No")

    fine_history2 = FineHistory(dni_person=45761873, fine="No", type_fine="", description_fine="", paid="")

    fine_history_str = fine_history1.__str__()
    print(fine_history_str)

    are_equal_fine_history = fine_history1.__eq__(fine_history2)
    print(are_equal_fine_history)

    # Prueba Mediator clas

    mediator = Mediator()

    mediator.add_person(person1)
    mediator.add_person(person2)

    mediator.add_education_history(edu_history1)
    mediator.add_education_history(edu_history2)

    mediator.add_fine_history(fine_history1)
    mediator.add_fine_history(fine_history2)

    # mediator.link_education_history_to_person(edu_history1, person1)
    # mediator.link_education_history_to_person(edu_history2, person2)

    mediator.link_fine_history_to_person(fine_history1, person1)
    mediator.link_fine_history_to_person(fine_history2, person2)

    # print(person1.education_history)
    # print(person2.education_history)

    print(person1.fine_history)
    print(person2.fine_history)

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

    found_fine_history = mediator.get_fine_history_by_dni(1043638720)
    if found_fine_history:
        print(found_fine_history.dni_person, found_fine_history.fine,
              found_fine_history.type_fine, found_fine_history.description_fine,
              found_fine_history.paid)
    else:
        print("Fine history not found")
