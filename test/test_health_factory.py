import unittest
from logic.health_factory import HealthFactory
from logic.agency_factory import agency1
from logic.health_agency import medical_history1, HealthAgency
from logic.medical_history import MedicalHistory


class TestHealthFactory(unittest.TestCase):
    health_factory = HealthFactory()
    health_agency = health_factory.create_agency(agency=agency1, medical_history=medical_history1)

    data = {"dni_person": 1043638720, "type_blood": "O+", "pathologies": None,
            "description_treatment": "Wound healing", "doctor_charge": "Kevin Rodriguez", "day": 5, "month": 10,
            "year": 2023}
    medical_history = health_factory.create_history(**data)

    def test_instance(self):
        self.assertIsInstance(self.health_factory, HealthFactory, 'Its\'s a instance!')

    def test_create_agency(self):
        self.assertIsInstance(self.health_agency, HealthAgency, 'It\'s a instance!')

    def test_create_history(self):
        self.assertIsInstance(self.medical_history, MedicalHistory, 'It\'s a instance!')


if __name__ == '__main__':
    unittest.main()
