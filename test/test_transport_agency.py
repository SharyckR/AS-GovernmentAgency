import unittest
from logic.agency_factory import agency1, agency2
from logic.transport_agency import TransportAgency
from logic.fine_history import fine_history1, fine_history2
from logic.vehicle_history import vehicle_history1, vehicle_history2


class TestTransportAgency(unittest.TestCase):

    transport_agency = TransportAgency(agency=agency1, licence="No", type_licence="None",
                                       information_vehicle=vehicle_history2, information_fine=fine_history2)

    def test_instance(self):
        self.assertIsInstance(self.transport_agency, TransportAgency, 'It is an instance!')

    def test_to_dict(self):
        expected_dict = {
            "Agency": agency1.to_dict(),
            "Licence": "No",
            "Type of licence": "None",
            "Information vehicle": vehicle_history2.to_dict(),
            "Information fine": fine_history2.to_dict()
        }
        self.assertEqual(self.transport_agency.to_dict(), expected_dict)

    def test_str(self):
        expected_str = (f'Agency: {agency1.__str__()}, Licence: {"No"}, Type of licence: {"None"}, '
                        f'Information vehicle: {vehicle_history2}, Information fine: {fine_history2}')
        self.assertEqual(str(self.transport_agency), expected_str)

    def test_eq(self):
        transport_agency1 = TransportAgency(agency=agency1, licence="No", type_licence="None",
                                            information_vehicle=vehicle_history2, information_fine=fine_history2)
        transport_agency2 = TransportAgency(agency=agency1, licence="No", type_licence="None",
                                            information_vehicle=vehicle_history2, information_fine=fine_history2)
        transport_agency3 = TransportAgency(agency=agency2, licence="Yes", type_licence="B1",
                                            information_vehicle=vehicle_history1, information_fine=fine_history1)

        self.assertEqual(transport_agency1, transport_agency2)
        self.assertNotEqual(transport_agency1, transport_agency3)


if __name__ == '__main__':
    unittest.main()
