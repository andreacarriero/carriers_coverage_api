import pandas
import pyproj

from app import app

from toolbox.logger import get_logger
from toolbox.configuration_loader import AppConfiguration
from toolbox.database import db

from models.carriers import CarrierConnectivity

from modules.address_api import ReverseAddressApiParserFR, LocationResponse, NoResultsError

log = get_logger(__name__)
conf = AppConfiguration()
reverse_location_api = ReverseAddressApiParserFR()

def lamb2coord(lX, lY):
    """
    Converts from Lambert 93 to GPS coordinates.

    Parameters
    ----------
    lX : int
        Lambert 93 X

    lY : int
        Lambert 93 Y

    Returns
    -------
    longitude : int

    latitude : int
    """
    lambert = pyproj.Proj('+proj=lcc +lat_1=49 +lat_2=44 +lat_0=46.5 +lon_0=3 +x_0=700000 +y_0=6600000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs')
    wgs84 = pyproj.Proj('+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs')
    long, lat = pyproj.transform(lambert, wgs84, lX, lY)
    return long, lat


def parse_and_populate(test_sandbox=False):
    """
    Parses and populates carriers connectivity table

    Parameters
    ----------
    test_sandbox : bool
        If True processes only 5 elements
    """

    csv_url = conf.get('franceCarriersConnectivityCSVURL')

    log.info('Getting and parsing data from %s' % csv_url)
    data = pandas.read_csv(
        csv_url,
        sep = ';',
        dtype = {
            'Operateur': str,
            '2G': bool,
            '3G': bool,
            '4G': bool
        }
    )
    
    with app.app_context():
        ######################################
        # God forgive me for this hardcoding #
        ######################################
        
        data_matrix = data.as_matrix()

        if test_sandbox:
            data_matrix = data_matrix[:5] # speedup testing

        for row in data_matrix:
            mcc_mnc = row[0]
            log.info('Processing carrier %s' % mcc_mnc)
            
            lX = row[1]
            lY = row[2]
            cX, cY = lamb2coord(lX, lY)

            try:
                reverse_location = reverse_location_api.search(cY, cX)
            except NoResultsError:
                reverse_location = LocationResponse(None,None,None,None,None).serialize()

            carrier_connectivity = CarrierConnectivity(
                mcc_mnc,
                cX,
                cY,
                reverse_location['label'],
                reverse_location['context'],
                reverse_location['city'],
                row[3],
                row[4],
                row[5]
            )
            db.session.add(carrier_connectivity)
            db.session.commit()