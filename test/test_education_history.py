import unittest
from logic.education_history import EducationHistory, edu_history1
from logic.address import address1


class TestEducationHistory(unittest.TestCase):
    edu_history = EducationHistory(
        id_history=10, dni_person=1412414, education='Bachiller',
        name_institution='Sena', location=address1, title_obtained='Engineering',
        day=15, month=12, year=1980)

    def test_instance(self) -> None:
        self.assertIsInstance(self.edu_history, EducationHistory, 'It\'s instance')

    def test_to_dict(self) -> None:
        expected = {'1412414': {'academic_achievements': 'None',
                                'date_graduation': '1980-12-15',
                                'education': 'Bachiller',
                                'id_history': 10,
                                'location': {'apartment': 'Apt 3B',
                                             'country': 'Country Land',
                                             'department': 'State Ville',
                                             'locality': 'City Ville',
                                             'number': 5,
                                             'postal_code': '1010',
                                             'street': '123 Main St'},
                                'name_institution': 'Sena',
                                'title_obtained': 'Engineering'}}
        self.assertEqual(self.edu_history.to_dict(), expected, 'They are equals')

    def test__eq__(self) -> None:
        self.assertFalse(self.edu_history.__eq__(edu_history1), 'The Educational histories aren\'t equals')

    def test__str__(self) -> None:
        expected = ("ID History: 10, DNI Person: 1412414, Level of Education: 'Bachiller', "
                    'Institution Name: \'Sena\', Location: "(Street: \'123 Main St\', Number: 5, '
                    "Apartment: 'Apt 3B', Postal Code: '1010', Locality: 'City Ville', "
                    'Department: \'Apt 3B\', Country: \'Country Land\')", Title Obtained: '
                    "'Engineering', Academic Achievements: 'None', Date Graduation: 15 - 12 - "
                    '1980\n')
        self.assertEqual(self.edu_history.__str__(), expected, 'They are equals')


if __name__ == '__main__':
    unittest.main()
