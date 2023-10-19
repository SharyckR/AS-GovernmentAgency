import unittest
from logic.vehicle_history import *


class TestVehicleHistory(unittest.TestCase):

    def test_instance(self):
        self.assertIsInstance(vehicle_history1, VehicleHistory, 'It is an instance!')

    def test_to_dict(self):
        expected_dict = {
            "DNI Person": 1043638720,
            "License?": "Yes",
            "Type of license": "A2",
            "Vehicle?": "Yes",
            "Type of vehicle": "Car",
            "Description of the Vehicle": "Mazda2",
            "Plate of the vehicle": "BJU-521"
        }
        self.assertEqual(vehicle_history1.to_dict(), expected_dict)

    def test_str(self):
        expected_str = (f'(Dni: {1043638720}, Does the person have a license?: {"Yes"}, Type of license: {"A2"}, '
                        f'Does the person have a vehicle?: {"Yes"}, Type of vehicle: {"Car"}, '
                        f'Description of the Vehicle: {"Mazda2"}, Plate of the vehicle: {"BJU-521"})')
        self.assertEqual(str(vehicle_history1), expected_str)

    def test_eq(self):
        self.assertEqual(vehicle_history1, vehicle_history1)
        self.assertNotEqual(vehicle_history1, vehicle_history2)


if __name__ == '__main__':
    unittest.main()
