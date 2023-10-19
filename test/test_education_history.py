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
        self.assertEqual(self.edu_history.to_dict(), {
            "DNI Person": 1412414,
            "Level of Education": 'Bachiller',
            "Institution Name": 'Sena',
            "Address": {
                "Street": '123 Main St',
                "Number": 5,
                "Apartment": 'Apt 3B',
                "Postal Code": '1010',
                "Locality": 'City Ville',
                "Department": 'State Ville',
                "Country": 'Country Land'
            },
            "Title Obtained": 'Engineering',
            "Date of graduation": '1980-12-15'
        }, 'They are equals')

    def test__eq__(self) -> None:
        self.assertFalse(self.edu_history.__eq__(edu_history1), 'The Educational histories aren\'t equals')

    def test__str__(self) -> None:
        self.assertEqual(self.edu_history.__str__(),
                         'DNI Person: 1412414, Level of Education: Bachiller, '
                         'Institution Name: Sena, Location: (123 Main St, 5, Apt 3B, 1010, '
                         'City Ville, State Ville, Country Land), '
                         'Title Obtained: Engineering, Date Graduation: 15 - 12 - 1980',
                         'They are equals')


if __name__ == '__main__':
    unittest.main()
