from toolbox.database import db
from toolbox.logger import get_logger

log = get_logger(__name__)

class Carrier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mcc_mnc = db.Column(db.String(5), unique=True)
    name = db.Column(db.String(20))

    def __init__(self, mcc_mnc, name):
        self.mcc_mnc = mcc_mnc
        self.name = name

class CarrierConnectivity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mcc_mnc = db.Column(db.String(5))
    coord_x = db.Column(db.Float) # float --> 8 bytes --> 1.7m precision
    coord_y = db.Column(db.Float) # float --> 8 bytes --> 1.7m precision
    conn_2G = db.Column(db.Boolean)
    conn_3G = db.Column(db.Boolean)
    conn_4G = db.Column(db.Boolean)

    location_label = db.Column(db.String(50))
    location_context = db.Column(db.String(50))
    location_city = db.Column(db.String(50))

    def __init__(
        self,
        mcc_mnc,
        coord_x,
        coord_y,
        location_label,
        location_context,
        location_city,
        conn_2G=False,
        conn_3G=False,
        conn_4G=False
    ):
        self.mcc_mnc = mcc_mnc
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.conn_2G = conn_2G
        self.conn_3G = conn_3G
        self.conn_4G = conn_4G
        self.location_label = location_label
        self.location_context = location_context
        self.location_city = location_city

def get_connectivity_in_city(city):
    log.info("Getting connectivity details in %s" % city)
    results = {}

    for carrier in Carrier.query.filter(Carrier.name != None).all():
        log.info("Analyzing %s in %s" % (carrier.name, city))
        
        if not results.get(carrier.name):
            results[carrier.name] = {'2G': False, '3G': False, '4G': False}
        
        connectivities = CarrierConnectivity.query.filter_by(mcc_mnc = carrier.mcc_mnc, location_city = city).all()
        for connectivity in connectivities:
            log.info("Analyzing connectivity for %s in %s, %s" % (carrier.name, connectivity.location_label, city))
            if connectivity.conn_2G:
                log.info("%s has 2G connection in %s, %s" % (carrier.name, connectivity.location_label, city))
                results[carrier.name]['2G'] = True
            if connectivity.conn_3G:
                log.info("%s has 3G connection in %s, %s" % (carrier.name, connectivity.location_label, city))
                results[carrier.name]['3G'] = True
            if connectivity.conn_4G:
                log.info("%s has 4G connection in %s, %s" % (carrier.name, connectivity.location_label, city))
                results[carrier.name]['4G'] = True

            if results[carrier.name]['2G'] and results[carrier.name]['3G'] and results[carrier.name]['4G']:
                log.info("%s has ALL the connectivities in %s" % (carrier.name, city))
                break

    return results

