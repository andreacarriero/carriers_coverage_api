from toolbox.database import db

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

    def __init__(self, mcc_mnc, coord_x, coord_y, conn_2G=False, conn_3G=False, conn_4G=False):
        self.mcc_mnc = mcc_mnc
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.conn_2G = conn_2G
        self.conn_3G = conn_3G
        self.conn_4G = conn_4G