import pandas
from sqlalchemy import exc

from app import app

from toolbox.logger import get_logger
from toolbox.configuration_loader import AppConfiguration
from toolbox.database import db

from models.carriers import Carrier

log = get_logger(__name__)
conf = AppConfiguration()

def parse_and_populate():
    wiki_url = conf.get('franceWikiMNCURL')

    log.info('Getting and parsing tables from %s' % wiki_url)
    tables = pandas.read_html(wiki_url)
    carriers_table = tables[0].as_matrix()

    with app.app_context():
        ######################################
        # God forgive me for this hardcoding #
        ######################################
        
        for row in carriers_table[1:]:
            mcc_mnc = row[0] + row[1]
            carrier_name = row[2]

            log.info("Processing %s" % carrier_name)
            try:
                carrier = Carrier(mcc_mnc, carrier_name)
                db.session.add(carrier)
                db.session.commit()
            except (exc.IntegrityError, exc.InvalidRequestError):
                log.info("Carrier %s already present, ignoring" % carrier_name)
