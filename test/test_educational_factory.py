import unittest
from logic.educational_factory import EducationalFactory, EducationalAgency
from logic.agency_factory import agency1
from logic.education_history import EducationHistory, edu_history1
from logic.address import address1


class TestEducationalFactory(unittest.TestCase):
    educational_factory = EducationalFactory()
    educational_agency = educational_factory.create_agency(agency1, edu_history1,
                                                           ["Best students", "First places",
                                                            "More successful graduates"])
    educational_history = educational_factory.create_history(
        10, 'Professional', 'Sena', address1, 'Engineering', 15, 4, 2015)

    def test_instance(self) -> None:
        self.assertIsInstance(self.educational_factory, EducationalFactory, 'It\'s instance!')

    def test_create_agency(self) -> None:
        self.assertIsInstance(self.educational_agency, EducationalAgency, 'It\'s instance!')

    def test_create_history(self) -> None:
        self.assertIsInstance(self.educational_history, EducationHistory, 'It\'s instance!')


if __name__ == '__main__':
    unittest.main()
