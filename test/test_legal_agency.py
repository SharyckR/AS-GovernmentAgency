import unittest
from logic.agency_factory import agency1, agency2
from logic.legal_agency import LegalAgency
from logic.case_history import case_history1, case_history2


class TestLegalAgency(unittest.TestCase):
    legal_agency = LegalAgency(agency=agency1, case_histories=[case_history1])

    def test_instance(self):
        self.assertIsInstance(self.legal_agency, LegalAgency, 'It is an instance!')

    def test_to_dict(self):
        expected_dict = {
            "965816": {"agency": agency1.to_dict(),
                       "case_history": case_history1.to_dict()}
        }
        self.assertEqual(expected_dict, self.legal_agency.to_dict(), 'They are equals!')

    def test__str__(self):
        expected_str = f'Agency: {str(agency1)}, Case History: {case_history1.__str__()}'
        self.assertEqual(expected_str, self.legal_agency.__str__(), 'They are equals!')

    def test__eq__(self):
        legal_agency1 = LegalAgency(agency=agency1, case_histories=[case_history1])
        legal_agency2 = LegalAgency(agency=agency1, case_histories=[case_history1])
        legal_agency3 = LegalAgency(agency=agency2, case_histories=[case_history2])

        self.assertTrue(legal_agency1.__eq__(legal_agency2), 'They are equals!')
        self.assertFalse(legal_agency1.__eq__(legal_agency3), 'They are not equals!')


if __name__ == '__main__':
    unittest.main()
