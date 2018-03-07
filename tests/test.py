import unittest, json
from app import app
from toolbox.database import db
from toolbox.configuration_loader import AppConfiguration

from data_processing import populate_carriers_connectivity
from models.carriers import CarrierConnectivity

from data_processing import populate_carriers
from models.carriers import Carrier

conf = AppConfiguration()

class TestCase(unittest.TestCase):

    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
        app.testing = True
        app.config['DEBUG'] = False
        with app.app_context():
            db.init_app(app)
            db.create_all()
        self.client = app.test_client()
        self.app_instance = app

        self._parse_and_populate_carriers()
        self._parse_and_populate_carriers_connectivity()

    def _parse_and_populate_carriers(self):
        populate_carriers.parse_and_populate()
        with self.app_instance.test_request_context():
            first_carrier = Carrier.query.first()
        self.assertIsNotNone(first_carrier)

    def _parse_and_populate_carriers_connectivity(self):
        populate_carriers_connectivity.parse_and_populate(test_sandbox=True)
        with self.app_instance.test_request_context():
            first_carrier_connectivity = CarrierConnectivity.query.first()
        self.assertIsNotNone(first_carrier_connectivity)

    def test_lambert93_to_coordinates(self):
        lX = 102980
        lY = 6847973

        cX, cY = populate_carriers_connectivity.lamb2coord(lX, lY)

        self.assertEqual(cX, -5.088856115301341)
        self.assertEqual(cY, 48.45657455881529)

    def test_legit_api_request(self):
        r = self.app_instance.test_client().get('/', query_string={'q': 'Ouessant'})
        self.assertEqual(r.status_code, 200)
        rj = json.loads(r.data)
        self.assertEqual(rj['meta']['location']['city'], 'Ouessant')
        for carrier in conf.get('carriersToShow'):
            self.assertIn(carrier, rj)

    def test_legit_api_request_for_all_carriers(self):
        r = self.app_instance.test_client().get('/', query_string={'q': 'Ouessant', 'all': True})
        self.assertEqual(r.status_code, 200)
        rj = json.loads(r.data)
        self.assertEqual(rj['meta']['location']['city'], 'Ouessant')
        with self.app_instance.test_request_context():
            for carrier in Carrier.query.filter(Carrier.name != None).all():
                self.assertIn(carrier.name, rj)

    def test_bad_api_request(self):
        r = self.app_instance.test_client().get('/', query_string={'query': 'Ouessant', 'all': True})
        self.assertEqual(r.status_code, 400)

    def test_wrong_place_api_request(self):
        r = self.app_instance.test_client().get('/', query_string={'q': 'porto cesareo, lecce, italy', 'all': True})
        self.assertEqual(r.status_code, 400)