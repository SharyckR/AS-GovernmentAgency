import unittest
from logic.case_history import *


class TestCaseHistory(unittest.TestCase):

    def test_instance(self):
        self.assertIsInstance(case_history1, CaseHistory, 'It is an instance!')

    def test_to_dict(self):
        expected_dict = {
            "1043638720": {
                "id_history": 13,
                "case": "Heist",
                "arrested": "Yes",
                "description_case": "Stole a necklace",
                "jurisdiction": "Disciplinary",
                "date_arrested": "2021-05-15",
                "lawyer": "Cristian Arroyo"
            }}
        self.assertEqual(expected_dict, case_history1.to_dict(), 'They are equals!')

    def test__str__(self):
        expected_str = ("ID History: 13, DNI Person: 1043638720, Case: 'Heist', Arrested: 'Yes', Description of "
                        "case: 'Stole a necklace', Jurisdiction: 'Disciplinary', Date arrested: 2021 - 5 - 15, "
                        "Lawyer in Charge: 'Cristian Arroyo'")

        self.assertEqual(expected_str, case_history1.__str__(), 'They are equals!')

    def test__eq__(self):
        case_history = CaseHistory(
            id_history=13, dni_person=1043638720, case="Heist", arrested="Yes", description_case="Stole a necklace",
            jurisdiction="Disciplinary", day=15, year=2021, month=5, lawyer="Cristian Arroyo")
        self.assertTrue(case_history1.__eq__(case_history), 'They are equals!')
        self.assertFalse(case_history1.__eq__(case_history2), 'They are not equals!')


if __name__ == '__main__':
    unittest.main()
