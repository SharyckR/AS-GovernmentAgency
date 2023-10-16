import unittest
from controller.mediator import Mediator
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

    person_data = {"id_entity": 652147963, "type_id_entity": "C.C.", "dni": 12345678, "type": "C.C.", "name": "Andrea",
                   "last_name": "Smith", "phone": 3165222657, "address": address}
    person = Person(**person_data)

    education_history_data = {"dni_person": 12345678, "education": "University",
                              "name_institution": "Massachusetts Institute of Technology",
                              "location": address1, "title_obtained": "Technological in systems",
                              "day": 13, "month": 10, "year": 2020}
    education_history = EducationHistory(**education_history_data)

    fine_history_data = {"dni_person": 12345678, "fine": "No", "type_fine": None,
                         "description_fine": None, "paid": None}
    fine_history = FineHistory(**fine_history_data)

    vehicle_history_data = {"dni_person": 12345678, "licence": "Yes", "type_licence": "B1", "vehicle": "Yes",
                            "type_vehicle": "Truck", "description_vehicle": "White", "plate_vehicle": "KIL-849"}
    vehicle_history = VehicleHistory(**vehicle_history_data)

    case_history_data = {"dni_person": 12345678, "case": "Fight", "arrested": "No",
                         "description_case": "Fight in a bar", "jurisdiction": "Police", "day": None, "year": None,
                         "month": None}
    case_history = CaseHistory(**case_history_data)

    medical_history_data = {"dni_person": 12345678, "type_blood": "AB", "pathologies": None,
                            "description_treatment": "Fall in stairs", "doctor_charge": "Dr. Ortiz",
                            "day": 9, "month": 5, "year": 2023}
    medical_history = MedicalHistory(**medical_history_data)

    def test_add_person(self):
        mediator = Mediator()

        mediator.add_person(TestMediator.person)

        self.assertEqual(len(mediator.persons), 1)
        self.assertEqual(mediator.persons[0]["DNI Person"], 12345678)

    def test_add_education_history(self):
        mediator = Mediator()

        mediator.add_education_history(TestMediator.education_history)

        self.assertEqual(len(mediator.education_histories), 1)
        self.assertEqual(mediator.education_histories[0]["DNI Person"], 12345678)

    def test_add_fine_history(self):
        mediator = Mediator()

        mediator.add_fine_history(TestMediator.fine_history)

        self.assertEqual(len(mediator.education_histories), 1)
        self.assertEqual(mediator.fine_histories[0]["DNI Person"], 12345678)

    def test_add_vehicle_history(self):
        mediator = Mediator()

        mediator.add_vehicle_history(TestMediator.vehicle_history)

        self.assertEqual(len(mediator.vehicle_histories), 1)
        self.assertEqual(mediator.vehicle_histories[0]["DNI Person"], 12345678)

    def test_add_case_history(self):
        mediator = Mediator()

        mediator.add_case_history(TestMediator.case_history)

        self.assertEqual(len(mediator.case_histories), 1)
        self.assertEqual(mediator.case_histories[0]["DNI Person"], 12345678)

    def test_add_medical_history(self):
        mediator = Mediator()

        mediator.add_medical_history(TestMediator.medical_history)

        self.assertEqual(len(mediator.medical_histories), 1)
        self.assertEqual(mediator.medical_histories[0]["DNI Person"], 12345678)

    def test_link_education_history_to_person(self):
        mediator = Mediator()

        mediator.link_education_history_to_person(TestMediator.education_history, TestMediator.person)

        self.assertEqual(len(mediator.education_histories), 1)
        self.assertEqual(mediator.education_histories[0]["DNI Person"], 12345678)

    def test_link_fine_history_to_person(self):
        mediator = Mediator()

        mediator.link_fine_history_to_person(TestMediator.fine_history, TestMediator.person)

        self.assertEqual(len(mediator.fine_histories), 1)
        self.assertEqual(mediator.fine_histories[0]["DNI Person"], 12345678)

    def test_link_vehicle_history_to_person(self):
        mediator = Mediator()

        mediator.link_vehicle_history_to_person(TestMediator.vehicle_history, TestMediator.person)

        self.assertEqual(len(mediator.vehicle_histories), 1)
        self.assertEqual(mediator.vehicle_histories[0]["DNI Person"], 12345678)

    def test_link_case_history_to_person(self):
        mediator = Mediator()

        mediator.link_case_history_to_person(TestMediator.case_history, TestMediator.person)

        self.assertEqual(len(mediator.case_histories), 1)
        self.assertEqual(mediator.case_histories[0]["DNI Person"], 12345678)

    def test_link_medical_history_to_person(self):
        mediator = Mediator()

        mediator.link_medical_history_to_person(TestMediator.medical_history, TestMediator.person)

        self.assertEqual(len(mediator.medical_histories), 1)
        self.assertEqual(mediator.medical_histories[0]["DNI Person"], 12345678)


if __name__ == '__main__':
    unittest.main()
