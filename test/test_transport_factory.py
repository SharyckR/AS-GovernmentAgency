import unittest
from logic.agency_factory import agency1
from logic.transport_agency import TransportAgency
from logic.transport_factory import TransportFactory
from logic.fine_history import *
from logic.vehicle_history import *


class TestTransportFactory(unittest.TestCase):
    transport_factory = TransportFactory()
    transport_agency = transport_factory.create_agency(agency1, vehicle_history1, fine_history1)
    vehicle_inf = {"id_history": 13, "dni_person": 1043638720, "licence": "Yes", "type_licence": "A2", "vehicle": "Yes",
                   "type_vehicle": "Car",
                   "description_vehicle": "Mazda2", "plate_vehicle": "BJU-521"
                   }
    fine_inf = {"id_history": 14, "dni_person": 1043638720, "fine": "Yes", "type_fine": "Fine for high speed",
                "description_fine": "The person was going more than 100k/h", "paid": "No"}
    vehicle_history, fine_history = transport_factory.create_history(vehicle_inf=vehicle_inf, fine_inf=fine_inf)

    def test_instance(self):
        self.assertIsInstance(self.transport_factory, TransportFactory, 'It is an instance!')

    def test_create_agency(self):
        self.assertIsInstance(self.transport_agency, TransportAgency, 'It is an instance!')

    def test_create_history(self):
        self.assertIsInstance(self.fine_history, FineHistory, 'It is an instance!')
        self.assertIsInstance(self.vehicle_history, VehicleHistory, 'It is an instance!')


if __name__ == '__main__':
    unittest.main()
