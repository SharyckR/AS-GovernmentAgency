import unittest
from logic.flyweight_address import AddressFlyweight
from logic.flyweight_address import AddressFlyweightFactory
from logic.flyweight_address import get_key
from logic.address import address1


class TestAddressFlyweight(unittest.TestCase):
    def test_get_key(self):
        address_test = address1
        state = [str(address_test)]
        result = get_key(state)
        expected = str(address_test)
        self.assertEqual(result, expected)


class TestAddressFlyweightFactory(unittest.TestCase):
    factory = AddressFlyweightFactory()

    def test_assign_flyweights(self):
        initial_states = [
            ["The cross", 10, "Apt 38B", "1010", "Aqueous", "Cundinamarca", "Colombia"],
            ["The cross", 10, "Apt 5C", "1010", "Aqueous", "Cundinamarca", "Colombia"],
        ]
        self.factory.assign_flyweights(initial_states)
        self.assertEqual(len(self.factory.flyweights), 2)

    def test_get_flyweight(self):
        self.factory.flyweights = {
            "Example Key": AddressFlyweight(
                shared_state=["The cross", 10, "Apt 38B", "1010", "Aqueous", "Cundinamarca", "Colombia"])
        }
        shared_state = ["The cross", 10, "Apt 38B", "1010", "Aqueous", "Cundinamarca",
                        "Colombia"]
        result = self.factory.get_flyweight(shared_state)
        self.assertIsInstance(result, AddressFlyweight)


if __name__ == '__main__':
    unittest.main()
