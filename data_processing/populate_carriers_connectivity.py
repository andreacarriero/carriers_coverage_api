import pandas
import pyproj

from app import app

from toolbox.logger import get_logger
from toolbox.configuration_loader import AppConfiguration
from toolbox.database import db

from models.carriers import CarrierConnectivity

log = get_logger(__name__)
conf = AppConfiguration()

def lamb2coord(lX, lY):
    lambert = pyproj.Proj('+proj=lcc +lat_1=49 +lat_2=44 +lat_0=46.5 +lon_0=3 +x_0=700000 +y_0=6600000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs')
    wgs84 = pyproj.Proj('+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs')
    long, lat = pyproj.transform(lambert, wgs84, lX, lY)
    return long, lat


def parse_and_populate():
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
        for row in data_matrix:
            mcc_mnc = row[0]
            log.info('Processing carrier %s' % mcc_mnc)
            
            lX = row[1]
            lY = row[2]
            cX, cY = lamb2coord(lX, lY)

            carrier_connectivity = CarrierConnectivity(
                mcc_mnc,
                cX,
                cY,
                row[3],
                row[4],
                row[5]
            )
            db.session.add(carrier_connectivity)
            db.session.commit()