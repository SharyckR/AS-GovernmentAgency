import unittest
from logic.vehicle_history import *


class TestVehicleHistory(unittest.TestCase):
    vehicle = VehicleHistory(id_history=13, dni_person=1043638720, licence="Yes", type_licence="A2", vehicle="Yes",
                             type_vehicle="Car", description_vehicle="Mazda2", plate_vehicle="BJU-521")

    def test_instance(self):
        self.assertIsInstance(vehicle_history1, VehicleHistory, 'It is an instance!')

    def test_to_dict(self):
        expected_dict = {'description_vehicle': 'Mazda2',
                         'dni_person': 1043638720,
                         'id_history': 13,
                         'licence': 'Yes',
                         'plate_vehicle': 'BJU-521',
                         'type_licence': 'A2',
                         'type_vehicle': 'Car',
                         'vehicle': 'Yes'}
        self.assertEqual(expected_dict, vehicle_history1.to_dict(), 'They are equals!')

    def test__str__(self):
        expected_str = ("ID History: 13 Dni: 1043638720, Does the person have a license?: 'Yes', Type "
                        "of license: 'A2', Does the person have a vehicle?: 'Yes', Type of vehicle: "
                        "'Car', Description of the Vehicle: 'Mazda2', Plate of the vehicle: 'BJU-521'")
        self.assertEqual(expected_str, self.vehicle.__str__(), 'They are equals!')

    def test__eq__(self):
        self.assertTrue(self.vehicle.__eq__(vehicle_history1), 'They are equals!')
        self.assertFalse(self.vehicle.__eq__(vehicle_history2), 'They are not equals!')


if __name__ == '__main__':
    unittest.main()
