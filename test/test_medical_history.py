import unittest
from logic.medical_history import MedicalHistory, medical_history1


class TestMedicalHistory(unittest.TestCase):
    medical_history = MedicalHistory(
        dni_person=1043638720, type_blood="O+", pathologies="None", description_treatment="Wound healing",
        doctor_charge="Kevin Rodriguez", day=5, month=10, year=2023)

    def test_instance(self):
        self.assertIsInstance(self.medical_history, MedicalHistory, 'It\'s a instance')

    def test_to_dict(self):
        expected = {
            "DNI Person": 1043638720,
            "Type blood": "O+",
            "Pathologies": "None",
            "Description Treatment": "Wound healing",
            "Doctor in Charge": "Kevin Rodriguez",
            "Date treatment": '2023-10-05'
        }
        self.assertEqual(self.medical_history.to_dict(), expected, 'They are equals!')

    def test__eq__(self):
        self.assertTrue(self.medical_history.__eq__(medical_history1), 'They are equals!')

    def test__str__(self):
        expected = (
            'Dni: 1043638720, Type blood: O+, Pathologies: None, Description treatment: Wound healing, Doctor charge: '
            'Kevin Rodriguez, Date treatment: 2023 - 10 - 5'
        )
        self.assertEqual(self.medical_history.__str__(), expected, 'They are equals!')


if __name__ == '__main__':
    unittest.main()
