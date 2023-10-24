import unittest
from logic.agency_factory import agency1, agency2
from logic.transport_agency import TransportAgency
from logic.fine_history import fine_history1, fine_history2
from logic.vehicle_history import vehicle_history1, vehicle_history2


class TestTransportAgency(unittest.TestCase):

    transport_agency = TransportAgency(agency=agency1, information_vehicle=vehicle_history2,
                                       information_fine=fine_history2)

    def test_instance(self):
        self.assertIsInstance(self.transport_agency, TransportAgency, 'It is an instance!')

    def test_to_dict(self):
        expected_dict = {
            "965816": {
                "agency": agency1.to_dict(),
                "information_vehicle": vehicle_history2.to_dict(),
                "information_fine": fine_history2.to_dict()}
        }
        self.assertEqual(expected_dict, self.transport_agency.to_dict(), 'They are equals!')

    def test__str__(self):
        expected_str = (f'Agency: {str(agency1)}, Information Vehicle: {vehicle_history2.__str__()}, '
                        f'Information Fine: {fine_history2.__str__()}')
        print(expected_str)
        print(self.transport_agency.__str__())
        self.assertEqual(expected_str, self.transport_agency.__str__(), 'They are equals!')

    def test__eq__(self):
        transport_agency1 = TransportAgency(agency=agency1,
                                            information_vehicle=vehicle_history2, information_fine=fine_history2)
        transport_agency2 = TransportAgency(agency=agency1,
                                            information_vehicle=vehicle_history2, information_fine=fine_history2)
        transport_agency3 = TransportAgency(agency=agency2,
                                            information_vehicle=vehicle_history1, information_fine=fine_history1)

        self.assertTrue(transport_agency1.__eq__(transport_agency2), 'They are equals!')
        self.assertFalse(transport_agency1.__eq__(transport_agency3), 'They are not equals!')


if __name__ == '__main__':
    unittest.main()
