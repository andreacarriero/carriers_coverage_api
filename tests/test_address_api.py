import unittest

from modules.address_api import AddressApiParserFR, ReverseAddressApiParserFR
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
        self.assertAlmostEqual(result['label'], 'Port de Suffren, CHAMP DE MARS - TOUR EIFFEL 75015 Paris')
        self.assertAlmostEqual(result['context'], '75, Paris, Île-de-France')
        self.assertEqual(result['coordinates']['x'], 2.289644)
        self.assertEqual(result['coordinates']['y'], 48.856888)


class ReverseAddressApiFRTestCase(unittest.TestCase):
    def test_bad_parameters(self):
        api = ReverseAddressApiParserFR()
        with self.assertRaises(BadRequestError):
            api.search('x', 'y')

    def test_coordinates_outside_france(self):
        api = ReverseAddressApiParserFR()
        with self.assertRaises(NoResultsError):
            api.search(40.3541621, 18.1567849)

    def test_legit_place(self):
        api = ReverseAddressApiParserFR()
        response = api.search(48.8583736, 2.2922926)
        self.assertEqual(response['city'], 'Paris')
        self.assertAlmostEqual(response['label'], '9001 Port de Suffren 75007 Paris')
        self.assertAlmostEqual(response['context'], '75, Paris, Île-de-France')


        