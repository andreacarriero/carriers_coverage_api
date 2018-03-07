import unittest

from modules.address_api import AddressApiParserFR
from modules.address_api import RequestError, BadRequestError, NoResultsError, AddressAPIProviderError

class AddressApiFRTestCase(unittest.TestCase):
    def test_empty_search(self):
        api = AddressApiParserFR()
        with self.assertRaises(BadRequestError):
            api.search('')
    
    def test_bad_string(self):
        api = AddressApiParserFR()
        with self.assertRaises(NoResultsError):
            api.search('ajhsajkasjkhsakjhsakhkha')

    def test_legit_place(self):
        api = AddressApiParserFR()
        result = api.search('Tour Eiffel')
        self.assertEqual(result['city'], 'Paris')
        