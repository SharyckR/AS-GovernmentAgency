import unittest
from logic.health_agency import HealthAgency, health1
from logic.agency_factory import agency1
from logic.medical_history import medical_history1


class TestHealthAgency(unittest.TestCase):
    health_agency = HealthAgency(agency=agency1, medical_history=medical_history1)

    def test_instance(self):
        self.assertIsInstance(self.health_agency, HealthAgency)

    def test_to_dict(self):
        expected_dict = {'965816': {'agency': {'address': {'apartment': 'Apt 3B',
                                                           'country': 'Country Land',
                                                           'department': 'State Ville',
                                                           'locality': 'City Ville',
                                                           'number': 5,
                                                           'postal_code': '1010',
                                                           'street': '123 Main St'},
                                               'business_name': 'Tis er ium',
                                               'contact': '3145975012',
                                               'date_actualization': '2023-10-05',
                                               'entity': 'Legal entity',
                                               'id_entity': 965816,
                                               'nit': 52173},
                                    'medical_history': {'date_treatment': '2023-10-05',
                                                        'description_treatment': 'Wound healing',
                                                        'dni_person': 1043638720,
                                                        'doctor_charge': 'Kevin Rodriguez',
                                                        'id_history': 13,
                                                        'pathologies': 'None',
                                                        'type_blood': 'O+'}}}
        self.assertEqual(expected_dict, self.health_agency.to_dict(), 'They are equals!')

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
