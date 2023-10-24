import unittest
from logic.fine_history import *


class TestFineHistory(unittest.TestCase):
    fine_history = FineHistory(id_history=14, dni_person=1043638720, fine="Yes", type_fine="Fine for high speed",
                               description_fine="The person was going more than 100k/h", paid="No")

    def test_instance(self):
        self.assertIsInstance(self.fine_history, FineHistory, 'It is an instance!')

    def test_to_dict(self):
        expected_dict = {'description_fine': 'The person was going more than 100k/h',
                         'dni_person': 1043638720,
                         'fine': 'Yes',
                         'id_history': 14,
                         'paid': 'No',
                         'type_fine': 'Fine for high speed'}
        self.assertEqual(expected_dict, self.fine_history.to_dict(), 'They are equals!')

    def test__str__(self):
        expected_str = ("ID History: 14, Dni: 1043638720, Has the person received a fine?: 'Yes', "
                        "Type of the fine: 'Fine for high speed', Description of the fine: 'The "
                        "person was going more than 100k/h', Has the person paid a fine?: 'No'")
        self.assertEqual(expected_str, str(self.fine_history), 'They are equals!')

    def test__eq__(self):
        self.assertTrue(self.fine_history.__eq__(fine_history1), 'They are equals!')
        self.assertFalse(self.fine_history.__eq__(fine_history2), 'They are not equals!')


if __name__ == '__main__':
    unittest.main()
