import unittest
from logic.flyweight_agency import AgencyFlyweight
from logic.flyweight_agency import AgencyFlyweightFactory
from logic.flyweight_address import get_key


class TestAgencyFlyweight(unittest.TestCase):

    def test_get_key(self):
        # Prueba con una lista de strings
        state = ["A", "B", "C"]
        result = get_key(state)
        self.assertEqual(result, "A_B_C")

        # Prueba con una lista de enteros
        state = [1, 2, 3]
        result = get_key(state)
        self.assertEqual(result, "1_2_3")

        # Prueba con una lista vacía
        state = []
        result = get_key(state)
        self.assertEqual(result, "")


class TestAgencyFlyweightFactory(unittest.TestCase):
    def test_assign_flyweights(self):
        factory = AgencyFlyweightFactory()
        initial_flyweights = [["A", "B", "C"], ["X", "Y", "Z"], ["1", "2", "3"]]
        factory.assign_flyweights(initial_flyweights)

        for state in initial_flyweights:
            key = get_key(state)
            flyweight = factory.flyweights.get(key)
            self.assertIsInstance(flyweight, AgencyFlyweight)
            self.assertEqual(flyweight.shared_state, state)

    def test_get_flyweight(self):
        factory = AgencyFlyweightFactory()
        shared_state1 = ["A", "B", "C"]
        shared_state2 = ["1", "2", "3"]
        flyweight1 = factory.get_flyweight(shared_state1)
        flyweight2 = factory.get_flyweight(shared_state2)

        self.assertIsInstance(flyweight1, AgencyFlyweight)
        self.assertEqual(flyweight1.shared_state, shared_state1)
        self.assertIsInstance(flyweight2, AgencyFlyweight)
        self.assertEqual(flyweight2.shared_state, shared_state2)


if __name__ == '__main__':
    unittest.main()
