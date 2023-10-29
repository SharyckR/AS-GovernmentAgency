import unittest
from logic.address import Address, address1, address2


class TestAddress(unittest.TestCase):
    data_address = {
        "street": '123 Main St', "number": 5, "apartment": 'Apt 3B', "postal_code": '1010', "locality": 'City Ville',
        "department": 'State Ville', "country": 'Country Land'
    }
    address = Address(**data_address)

    def test_instance(self):
        self.assertIsInstance(self.address, Address, 'It\'s a instance')

    def test__eq__(self):
        self.assertFalse(self.address.__eq__(address2), 'They are not equals')
        self.assertTrue(self.address.__eq__(address1), 'They are equals!')

    def test_address_to_dict(self):
        address = Address(street='123 Main St', number=5, apartment='Apt 3B', postal_code='1010', locality='City Ville',
                          department='State Ville', country='Country Land')

        expected_dict = {'apartment': 'Apt 3B',
                         'country': 'Country Land',
                         'department': 'State Ville',
                         'locality': 'City Ville',
                         'number': 5,
                         'postal_code': '1010',
                         'street': '123 Main St'}

        self.assertEqual(expected_dict, address.to_dict(), 'They are equals!')


if __name__ == '__main__':
    unittest.main()
