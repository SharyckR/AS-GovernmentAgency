import unittest
from logic.agency_factory import agency1
from logic.transport_agency import TransportAgency
from logic.transport_factory import TransportFactory
from logic.fine_history import *
from logic.vehicle_history import *


class TestTransportFactory(unittest.TestCase):

    transport_factory = TransportFactory()
    transport_agency = transport_factory.create_agency(agency1, "Yes", "A1",
                                                       vehicle_history1, fine_history1)
    vehicle_history, fine_history = transport_factory.create_history(dni_person=45761873, licence="Yes",
                                                                     type_licence="B1", vehicle="No",
                                                                     type_vehicle="None", description_vehicle="None",
                                                                     plate_vehicle=None, fine="Yes",
                                                                     type_fine="Exceed speed",
                                                                     description_fine="Was driving at 100 km/h",
                                                                     paid="Yes")

    def test_instance(self):
        self.assertIsInstance(self.transport_factory, TransportFactory, 'It is an instance!')

    def test_create_agency(self):
        self.assertIsInstance(self.transport_agency, TransportAgency, 'It is an instance!')

    def test_create_history(self):
        self.assertIsInstance(self.fine_history, FineHistory, 'It is an instance!')
        self.assertIsInstance(self.vehicle_history, VehicleHistory, 'It is an instance!')


if __name__ == '__main__':
    unittest.main()
