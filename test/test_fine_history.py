import unittest
from logic.fine_history import *


class TestFineHistory(unittest.TestCase):

    def test_instance(self):
        self.assertIsInstance(fine_history1, FineHistory, 'It is an instance!')

    def test_to_dict(self):
        expected_dict = {
            "DNI Person": 1043638720,
            "Fine?": "Yes",
            "Type of Fine": "Fine for high speed",
            "Description Fine": "The person was going more than 100k/h",
            "Paid?": "No"
        }
        self.assertEqual(fine_history1.to_dict(), expected_dict)

    def test_str(self):
        expected_str = (f'Dni: {1043638720}, Has the person received a fine?: {"Yes"}, '
                        f'Type of the fine: {"Fine for high speed"}, '
                        f'Description of the fine: {"The person was going more than 100k/h"}, '
                        f'Has the person paid a fine?: {"No"}')
        self.assertEqual(str(fine_history1), expected_str)

    def test_eq(self):
        self.assertEqual(fine_history1, fine_history1)
        self.assertNotEqual(fine_history1, fine_history2)


if __name__ == '__main__':
    unittest.main()
