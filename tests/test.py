import unittest
from app import app
from toolbox.database import db

from data_processing import populate_carriers_connectivity
from models.carriers import CarrierConnectivity

from data_processing import populate_carriers
from models.carriers import Carrier

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