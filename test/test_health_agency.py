import unittest
from logic.health_agency import HealthAgency, health1
from logic.agency_factory import agency1
from logic.medical_history import medical_history1


class TestHealthAgency(unittest.TestCase):
    health_agency = HealthAgency(agency=agency1, medical_history=medical_history1)

    def test_instance(self):
        self.assertIsInstance(self.health_agency, HealthAgency)

    def test_to_dict(self):
        self.assertEqual(self.health_agency.to_dict(), {
            "Agency": {
                'ID Entity': 965816,
                'Entity': 'Legal entity',
                'NIT': 52173,
                'Business Name': 'Tis er ium',
                'Contact': '3145975012',
                'Address': {
                    "Street": '123 Main St',
                    "Number": 5,
                    "Apartment": 'Apt 3B',
                    "Postal Code": '1010',
                    "Locality": 'City Ville',
                    "Department": 'State Ville',
                    "Country": 'Country Land'
                },
                'Date Actualization': '1999-01-01'
            },
            "Medical History":
                {
                    "DNI Person": 1043638720,
                    "Type blood": "O+",
                    "Pathologies": "None",
                    "Description Treatment": "Wound healing",
                    "Doctor in Charge": "Kevin Rodriguez",
                    "Date treatment":  '2023-10-05',
                }
        }, 'They are equals!')

    def test__eq__(self):
        self.assertTrue(self.health_agency.__eq__(health1), 'They are equals')

    def test__str__(self):
        self.assertTrue(self.__str__(), {
            'Agency information: {'
            'Id Agency: 965816, Entity: Legal entity, Nit: 52173, Business Name: Tis er ium, Contact (Phone or '
            'E-mail): 3145975012,'
            'Address: (123 Main St, 5, Apt 3B, 1010, City Ville, State Ville, Country Land) '
            ', Date Actualization: {5} - {10} - {2023}'
            '}, Medical History: {'
            'Dni: 1043638720, Type blood: O+, Pathologies: None, Description treatment: Wound healing, '
            'Doctor charge: Kevin Rodriguez, Date treatment: 5 - 10 - 2023}'
        })


if __name__ == '__main__':
    unittest.main()
