import unittest
from controller.mediator import *
from logic.person import Person
from logic.address import Address
from logic.education_history import EducationHistory
from logic.fine_history import FineHistory
from logic.vehicle_history import VehicleHistory
from logic.case_history import CaseHistory
from logic.medical_history import MedicalHistory


class TestMediator(unittest.TestCase):

    address_data = {"street": "123 Main St", "number": 5, "apartment": "Apt 3B", "postal_code": "1011",
                    "locality": "City Ville", "department": "State Ville", "country": "Country Land"}
    address = Address(**address_data)

    address1_data = {"street": "Massachusetts Ave", "number": 77, "apartment": "None", "postal_code": "MA 02139",
                     "locality": "None", "department": "Cambridge", "country": "EE.UU."}
    address1 = Address(**address1_data)

    person_data = {"username": 124230242, "id_entity": 2723723, "type_id_entity": "C.C.", "dni_person": 124230242,
                   "type": "C.C.", "name": "María", "last_name": "Sarmiento", "phone": 313242323, "address": address,
                   "day": 15, "month": 12, "year": 2004}
    person = Person(**person_data)

    education_history_data = {"dni_person": 124230242, "education": "University",
                              "name_institution": "Massachusetts Institute of Technology",
                              "location": address1, "title_obtained": "Technological in systems",
                              "day": 13, "month": 10, "year": 2020}
    education_history = EducationHistory(**education_history_data)

    fine_history_data = {"dni_person": 124230242, "fine": "No", "type_fine": None,
                         "description_fine": None, "paid": None}
    fine_history = FineHistory(**fine_history_data)

    vehicle_history_data = {"dni_person": 124230242, "licence": "Yes", "type_licence": "B1", "vehicle": "Yes",
                            "type_vehicle": "Truck", "description_vehicle": "White", "plate_vehicle": "KIL-849"}
    vehicle_history = VehicleHistory(**vehicle_history_data)

    case_history_data = {"dni_person": 124230242, "case": "Fight", "arrested": "No",
                         "description_case": "Fight in a bar", "jurisdiction": "Police", "day": 15, "year": 2023,
                         "month": 7}
    case_history = CaseHistory(**case_history_data)

    medical_history_data = {"dni_person": 124230242, "type_blood": "AB", "pathologies": None,
                            "description_treatment": "Fall in stairs", "doctor_charge": "Dr. Ortiz",
                            "day": 9, "month": 5, "year": 2023}
    medical_history = MedicalHistory(**medical_history_data)

    def test_add_person(self):
        mediator = Mediator()
        persons = mediator._persons

        mediator.add_person(TestMediator.person)

        self.assertEqual(persons[-1][f"{TestMediator.person.dni_person}"]["dni_person"], TestMediator.person.dni_person)

    def test_link_education_history_to_person(self):
        mediator = Mediator()

        mediator.link_education_history_to_person(TestMediator.person.dni_person, TestMediator.education_history)

        person_education = mediator._persons[-1].get("education_history")
        education_history_dict = TestMediator.education_history.to_dict()

        self.assertIsInstance(person_education, dict)
        self.assertEqual(person_education, education_history_dict)

    def test_link_fine_history_to_person(self):
        mediator = Mediator()

        mediator.link_fine_history_to_person(TestMediator.person.dni_person, TestMediator.fine_history)

        person_fine = mediator._persons[-1].get("fine_history")
        fine_history_dict = TestMediator.fine_history.to_dict()

        self.assertIsInstance(person_fine, dict)
        self.assertEqual(person_fine, fine_history_dict)

    def test_link_vehicle_history_to_person(self):
        mediator = Mediator()

        mediator.link_vehicle_history_to_person(TestMediator.person.dni_person, TestMediator.vehicle_history)

        person_vehicle = mediator._persons[-1].get("vehicle_history")
        vehicle_history_dict = TestMediator.vehicle_history.to_dict()

        self.assertIsInstance(person_vehicle, dict)
        self.assertEqual(person_vehicle, vehicle_history_dict)

    def test_link_case_history_to_person(self):
        mediator = Mediator()

        mediator.link_case_history_to_person(TestMediator.person.dni_person, TestMediator.case_history)

        person_case = mediator._persons[-1].get("case_history")
        case_history_dict = TestMediator.case_history.to_dict()

        self.assertIsInstance(person_case, dict)
        self.assertEqual(person_case, case_history_dict)

    def test_link_medical_history_to_person(self):
        mediator = Mediator()

        mediator.link_medical_history_to_person(TestMediator.person.dni_person, TestMediator.medical_history)

        medical_education = mediator._persons[-1].get("medical_history")
        medical_history_dict = TestMediator.medical_history.to_dict()

        self.assertIsInstance(medical_education, dict)
        self.assertEqual(medical_education, medical_history_dict)

    def test_get_person_info(self):
        mediator = Mediator()
        persons = mediator._persons

        get_person_info(TestMediator.person.dni_person)

        self.assertEqual(persons[-1][f"{TestMediator.person.dni_person}"]["dni_person"], TestMediator.person.dni_person)

    def test_get_educational_history(self):
        mediator = Mediator()

        education_histories = mediator._persons[-1][f"{TestMediator.person.dni_person}"]["education_history"]
        education_data = get_educational_history(TestMediator.person.dni_person)

        self.assertEqual(education_histories, education_data)

    def test_get_fine_history(self):
        mediator = Mediator()

        fine_histories = mediator._persons[-1][f"{TestMediator.person.dni_person}"]["fine_history"]
        fine_data = get_fine_history(TestMediator.person.dni_person)

        self.assertEqual(fine_histories, fine_data)

    def test_get_vehicle_history(self):
        mediator = Mediator()

        vehicle_histories = mediator._persons[-1][f"{TestMediator.person.dni_person}"]["vehicle_history"]
        vehicle_data = get_vehicle_history(TestMediator.person.dni_person)

        self.assertEqual(vehicle_histories, vehicle_data)

    def test_get_case_history(self):
        mediator = Mediator()

        case_histories = mediator._persons[-1][f"{TestMediator.person.dni_person}"]["case_history"]
        case_data = get_case_history(TestMediator.person.dni_person)

        self.assertEqual(case_histories, case_data)

    def test_get_medical_history(self):
        mediator = Mediator()

        medical_histories = mediator._persons[-1][f"{TestMediator.person.dni_person}"]["medical_history"]
        medical_data = get_medical_history(TestMediator.person.dni_person)

        self.assertEqual(medical_histories, medical_data)


if __name__ == '__main__':
    unittest.main()
