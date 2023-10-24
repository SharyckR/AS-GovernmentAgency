import unittest
from logic.agency_factory import agency1
from logic.legal_factory import LegalFactory, LegalAgency
from logic.case_history import CaseHistory, case_history1


class TestLegalFactory(unittest.TestCase):
    legal_factory = LegalFactory()
    legal_agency = legal_factory.create_agency(agency1, case_history1)
    data = {"dni_person": 45761873, "case": "Harassment", "arrested": "Yes",
            "description_case": "Harassment of woman in the park", "jurisdiction": "Jury",
            "day": 14, "month": 8, "year": 2020}
    case_history = legal_factory.create_history()

    def test_instance(self):
        self.assertIsInstance(self.legal_factory, LegalFactory, 'It is an instance!')

    def test_create_agency(self):
        self.assertIsInstance(self.legal_agency, LegalAgency, 'It is an instance!')

    def test_create_history(self):
        self.assertIsInstance(self.case_history, CaseHistory, 'It is an instance!')


if __name__ == '__main__':
    unittest.main()
