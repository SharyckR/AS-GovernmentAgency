import unittest
from logic.agency_factory import AgencyFactory
from logic.legal_entity import LegalEntity
from logic.address import address2
from logic.agency_factory import agency1, agency2


class TestAgencyFactory(unittest.TestCase):
    agency = {
        "username": "10290294", "id_entity": 10290294, "entity": LegalEntity(), "nit": 4224,
        "business_name": "Business Name", "contact": "31459750", "address": address2, "day": 5, "month": 10,
        "year": 2023
    }
    agency_factory = AgencyFactory(**agency)

    def test_instance(self):
        self.assertIsInstance(self.agency_factory, AgencyFactory, 'It\'s a instance')

    def test__eq__(self):
        self.assertFalse(self.agency_factory.__eq__(agency1), 'They are not equals!')
        self.assertTrue(self.agency_factory.__eq__(agency2), 'The are equals!')

    def test__str__(self):
        expected = ('Id Agency: 10290294, Entity: Type: Legal Entity, Nit: 4224, Business Name: '
                    "Business Name, Contact (Phone or E-mail): 31459750, Address: (Street: 'The "
                    "cross', Number: 10, Apartment: 'Apt 5C', Postal Code: '1010', Locality: "
                    "'Aqueous', Department: 'Apt 5C', Country: 'Colombia'), Date Actualization: 5 "
                    '- 10 - 2023\n')
        self.assertEqual(self.agency_factory.__str__(), expected, 'They are equals!')

    def test_agency_to_dict(self):
        expected_dict = {'address': {'apartment': 'Apt 5C',
                                     'country': 'Colombia',
                                     'department': 'Cundinamarca',
                                     'locality': 'Aqueous',
                                     'number': 10,
                                     'postal_code': '1010',
                                     'street': 'The cross'},
                         'business_name': 'Business Name',
                         'contact': '31459750',
                         'date_actualization': '2023-10-05',
                         'entity': {'type: Legal Entity, subtype: None'},
                         'id_entity': 10290294,
                         'nit': 4224}
        self.assertEqual(self.agency_factory.to_dict(), expected_dict, 'They are equals!')


if __name__ == '__main__':
    unittest.main()
