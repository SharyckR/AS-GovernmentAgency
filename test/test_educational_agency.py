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
        self.assertEqual(self.educational.to_dict(), {
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
            "Education History": {
                "DNI Person": 1043638720,
                "Level of Education": 'Secondary',
                "Institution Name": "Collage",
                "Address": {
                    "Street": '123 Main St',
                    "Number": 5,
                    "Apartment": 'Apt 3B',
                    "Postal Code": '1010',
                    "Locality": 'City Ville',
                    "Department": 'State Ville',
                    "Country": 'Country Land'
                },
                "Title Obtained": "Graduated",
                "Date of graduation": '2020-10-13'
            },
            "Academic Achievements": ['Good Students', 'Best in maths']
        })

    def test__str__(self) -> None:
        actual_result = self.educational.__str__()
        expected_result = (
            'Agency: '
            'Id Agency: {!r}, Entity: Type: Legal entity, Nit: {!r}, Business Name: Tis er ium, '
            'Contact (Phone or E-mail): {!r}, '
            'Address: (123 Main St, {!r}, Apt 3B, 1010, City Ville, State Ville, Country Land), '
            'Date Actualization: {!r} - {!r} - {!r}, '
            'Education History: DNI Person: 1043638720, Level of Education: '
            'Secondary, Institution Name: Collage, Location: (123 Main St, 5, '
            'Apt 3B, 1010, City Ville, State Ville, Country Land), '
            'Title Obtained: Graduated, Date Graduation: 13 - 10 - 2020, '
            'Academic achievements: {!r}'.format(
                965816, 52173, 3145975012, 5,
                5, 10, 2023, ['Good Students', 'Best in maths'])
        )
        self.assertEqual(actual_result, expected_result)

    def test__eq__(self) -> None:
        self.assertTrue(self.educational.__eq__(educational1))


if __name__ == '__main__':
    unittest.main()
