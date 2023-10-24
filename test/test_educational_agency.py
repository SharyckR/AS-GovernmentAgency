import unittest
from logic.educational_agency import EducationalAgency, educational1
from logic.agency_factory import agency1
from logic.education_history import edu_history1


class TestEducationalAgency(unittest.TestCase):
    educational = EducationalAgency(agency=agency1, education_history=edu_history1,
                                    academic_achievements=['Good Students', 'Best in maths'])

    def test_instance(self) -> None:
        self.assertIsInstance(self.educational, EducationalAgency, 'It\'s instance!')

    def test_to_dict(self) -> None:
        expected_dict = {'965816': {'academic_achievements': ['Good Students', 'Best in maths'],
                                    'agency': {'address': {'apartment': 'Apt 3B',
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
                                    'education_history': {'date_graduation': '2020-10-13',
                                                          'dni_person': 1043638720,
                                                          'education': 'Secondary',
                                                          'id_history': 40,
                                                          'location': {'apartment': 'Apt 3B',
                                                                       'country': 'Country Land',
                                                                       'department': 'State Ville',
                                                                       'locality': 'City Ville',
                                                                       'number': 5,
                                                                       'postal_code': '1010',
                                                                       'street': '123 Main St'},
                                                          'name_institution': 'Collage',
                                                          'title_obtained': 'Graduated'}}}
        self.assertEqual(expected_dict, self.educational.to_dict(), 'They are equals!')

    def test__str__(self) -> None:
        actual_result = self.educational.__str__()
        expected_result = (
            'Agency: Id Agency: 965816, Entity: Type: Legal entity, Nit: 52173, Business '
            'Name: Tis er ium, Contact (Phone or E-mail): 3145975012, Address: (Street: '
            "'123 Main St', Number: 5, Apartment: 'Apt 3B', Postal Code: '1010', "
            "Locality: 'City Ville', Department: 'Apt 3B', Country: 'Country Land'), Date "
            'Actualization: 5 - 10 - 2023, Education History: ID History: 40, DNI Person: '
            "1043638720, Level of Education: 'Secondary', Institution Name: 'Collage', "
            'Location: "(Street: \'123 Main St\', Number: 5, Apartment: \'Apt 3B\', '
            "Postal Code: '1010', Locality: 'City Ville', Department: 'Apt 3B', Country: "
            '\'Country Land\')", Title Obtained: \'Graduated\', Date Graduation: 13 - 10 '
            "- 2020, Academic achievements: ['Good Students', 'Best in maths']")

        self.assertEqual(expected_result, actual_result, 'They are equals!')

    def test__eq__(self) -> None:
        self.assertTrue(self.educational.__eq__(educational1), 'They are equals!')


if __name__ == '__main__':
    unittest.main()
