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

    address_data = {"street": "Santo Domingo", "number": 15, "apartment": "1", "postal_code": "14500",
                    "locality": "None", "department": "Bolivar", "country": "Colombia"}
    address = Address(**address_data)

    address1_data = {"street": "Massachusetts Ave", "number": 77, "apartment": "None", "postal_code": "MA 02139",
                     "locality": "None", "department": "Cambridge", "country": "EE.UU."}
    address1 = Address(**address1_data)

    person_data = {"id_entity": 2723723, "type_id_entity": "C.C.", "dni": 124230242, "type": "C.C.", "name": "María",
                   "last_name": "Sarmiento", "phone": 313242323, "address": address}
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
                         "description_case": "Fight in a bar", "jurisdiction": "Police", "day": None, "year": None,
                         "month": None}
    case_history = CaseHistory(**case_history_data)

    medical_history_data = {"dni_person": 124230242, "type_blood": "AB", "pathologies": None,
                            "description_treatment": "Fall in stairs", "doctor_charge": "Dr. Ortiz",
                            "day": 9, "month": 5, "year": 2023}
    medical_history = MedicalHistory(**medical_history_data)

    def test_add_person(self):
        mediator = Mediator()
        persons = mediator._Mediator__persons

        mediator.add_person(TestMediator.person)

        self.assertEqual(persons[0]["DNI Person"], 124230242)

    def test_link_education_history_to_person(self):
        mediator = Mediator()
        education_histories = mediator._Mediator__education_histories

        mediator.link_education_history_to_person(TestMediator.person.dni, TestMediator.education_history)

        self.assertEqual(education_histories[0]["DNI Person"], 124230242)

    def test_link_fine_history_to_person(self):
        mediator = Mediator()
        fine_histories = mediator._Mediator__fine_histories

        mediator.link_fine_history_to_person(TestMediator.person.dni, TestMediator.fine_history)

        self.assertEqual(fine_histories[0]["DNI Person"], 124230242)

    def test_link_vehicle_history_to_person(self):
        mediator = Mediator()
        vehicle_histories = mediator._Mediator__vehicle_histories

        mediator.link_vehicle_history_to_person(TestMediator.person.dni, TestMediator.vehicle_history)

        self.assertEqual(vehicle_histories[0]["DNI Person"], 124230242)

    def test_link_case_history_to_person(self):
        mediator = Mediator()
        case_histories = mediator._Mediator__case_histories

        mediator.link_case_history_to_person(TestMediator.person.dni, TestMediator.case_history)

        self.assertEqual(case_histories[0]["DNI Person"], 124230242)

    def test_link_medical_history_to_person(self):
        mediator = Mediator()
        medical_histories = mediator._Mediator__medical_histories

        mediator.link_medical_history_to_person(TestMediator.person.dni, TestMediator.medical_history)

        self.assertEqual(medical_histories[0]["DNI Person"], 124230242)

    def test_get_person_info(self):
        mediator = Mediator()
        persons = mediator._Mediator__persons

        get_person_info(TestMediator.person.dni)

        self.assertEqual(persons[0]["DNI Person"], 124230242)

    def test_get_educational_history(self):
        mediator = Mediator()
        education_histories = mediator._Mediator__education_histories

        get_educational_history(TestMediator.person.dni)

        self.assertEqual(education_histories[0]["DNI Person"], 124230242)

    def test_get_fine_history(self):
        mediator = Mediator()
        fine_histories = mediator._Mediator__fine_histories

        get_fine_history(TestMediator.person.dni)

        self.assertEqual(fine_histories[0]["DNI Person"], 124230242)

    def test_get_vehicle_history(self):
        mediator = Mediator()
        vehicle_histories = mediator._Mediator__vehicle_histories

        get_vehicle_history(TestMediator.person.dni)

        self.assertEqual(vehicle_histories[0]["DNI Person"], 124230242)

    def test_get_case_history(self):
        mediator = Mediator()
        case_histories = mediator._Mediator__case_histories

        get_case_history(TestMediator.person.dni)

        self.assertEqual(case_histories[0]["DNI Person"], 124230242)

    def get_medical_history(self):
        mediator = Mediator()
        medical_histories = mediator._Mediator__medical_histories

        get_medical_history(TestMediator.person.dni)

        self.assertEqual(medical_histories[0]["DNI Person"], 124230242)


if __name__ == '__main__':
    unittest.main()
