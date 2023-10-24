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
    data = {"id_history": 10, "dni_person": 14, "education": 'Professional', "name_institution": 'Sena',
            "location": address1, "title_obtained": 'Engineering', "day": 15, "month": 4, "year": 2015}
    educational_history = educational_factory.create_history(**data)

    def test_instance(self) -> None:
        self.assertIsInstance(self.educational_factory, EducationalFactory, 'It\'s instance!')

    def test_create_agency(self) -> None:
        self.assertIsInstance(self.educational_agency, EducationalAgency, 'It\'s instance!')

    def test_create_history(self) -> None:
        self.assertIsInstance(self.educational_history, EducationHistory, 'It\'s instance!')


if __name__ == '__main__':
    unittest.main()
