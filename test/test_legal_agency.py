import unittest
from logic.agency_factory import agency1, agency2
from logic.legal_agency import LegalAgency
from logic.case_history import case_history1, case_history2


class TestLegalAgency(unittest.TestCase):

    legal_agency = LegalAgency(agency=agency1, legal_history=case_history1)
    print(case_history1.__str__())

    def test_instance(self):
        self.assertIsInstance(self.legal_agency, LegalAgency, 'It is an instance!')

    def test_to_dict(self):
        print(case_history1.to_dict())
        expected_dict = {
            "Agency": agency1.to_dict(),
            "Case History": case_history1.to_dict()
        }
        self.assertEqual(self.legal_agency.to_dict(), expected_dict)

    def test_str(self):
        expected_str = f'(Agency: {str(agency1)}, Case History: {case_history1.__str__()})'
        self.assertEqual(str(self.legal_agency), expected_str)

    def test_eq(self):
        legal_agency1 = LegalAgency(agency=agency1, case_history=case_history1)
        legal_agency2 = LegalAgency(agency=agency1, case_history=case_history1)
        legal_agency3 = LegalAgency(agency=agency2, case_history=case_history2)

        self.assertEqual(legal_agency1, legal_agency2)
        self.assertNotEqual(legal_agency1, legal_agency3)


if __name__ == '__main__':
    unittest.main()
