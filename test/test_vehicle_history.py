import unittest
from logic.vehicle_history import *


class TestVehicleHistory(unittest.TestCase):
    vehicle = VehicleHistory(id_history=13, dni_person=1043638720, licence="Yes", number_licence=123456,
                             type_licence="A2", expedition_date="2020-05-11", expiration_date="2023-05-11",
                             vehicle="Yes", type_vehicle="Car", description_vehicle="Mazda2", plate_vehicle="BJU-521",
                             insurance=2020)

    def test_instance(self):
        self.assertIsInstance(vehicle_history1, VehicleHistory, 'It is an instance!')

    def test_to_dict(self):
        expected_dict = {"1043638720": {"id_history": 13,
                                        "licence": "Yes",
                                        "number_licence": 123456,
                                        "type_licence": "A2",
                                        "expedition_date": "2020-05-11",
                                        "expiration_date": "2023-05-11",
                                        "vehicle": "Yes",
                                        "type_vehicle": "Car",
                                        "description_vehicle": "Mazda2",
                                        "plate_vehicle": "BJU-521",
                                        "insurance": 2020}}
        self.assertEqual(vehicle_history1.to_dict(), expected_dict, 'They are equals!')

    def test__str__(self):
        expected_str = ("ID History: 13 Dni: 1043638720, Does the person have a license?: 'Yes', "
                        "Number Licence: 123456, Type of license: 'A2', Expedition Date: "
                        "'2020-05-11', Expiration Date: '2023-05-11', Does the person have a "
                        "vehicle?: 'Yes', Type of vehicle: 'Car', Description of the Vehicle: "
                        "'Mazda2', Plate of the vehicle: 'BJU-521', Insurance: 2020\n")
        self.assertEqual(expected_str, self.vehicle.__str__(), 'They are equals!')

    def test__eq__(self):
        self.assertTrue(self.vehicle.__eq__(vehicle_history1), 'They are equals!')
        self.assertFalse(self.vehicle.__eq__(vehicle_history2), 'They are not equals!')


if __name__ == '__main__':
    unittest.main()
