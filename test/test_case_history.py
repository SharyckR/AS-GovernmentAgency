import unittest
from logic.case_history import *


class TestCaseHistory(unittest.TestCase):

    def test_instance(self):
        self.assertIsInstance(case_history1, CaseHistory, 'It is an instance!')

    def test_to_dict(self):
        expected_dict = {
            "DNI Person": 1043638720,
            "Case": "Heist",
            "Arrested?": "Yes",
            "Description of Case": "Stole a necklace",
            "Jurisdiction": "Disciplinary",
            "Date arrested": "2021-05-15"
        }
        self.assertEqual(case_history1.to_dict(), expected_dict)

    def test_str(self):
        expected_str = (f'DNI Person: {1043638720}, Case: {"Heist"}, Arrested: {"Yes"}, '
                        f'Description of case: {"Stole a necklace"}, Jurisdiction: {"Disciplinary"}, '
                        f'Date arrested: {"2021 - 5 - 15"}')
        self.assertEqual(str(case_history1), expected_str)

    def test_eq(self):
        self.assertEqual(case_history1, case_history1)
        self.assertNotEqual(case_history1, case_history2)


if __name__ == '__main__':
    unittest.main()
