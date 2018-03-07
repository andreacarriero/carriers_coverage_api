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
    lambert93X = db.Column(db.String(7))
    lambert93Y = db.Column(db.String(7))
    conn_2G = db.Column(db.Boolean)
    conn_3G = db.Column(db.Boolean)
    conn_4G = db.Column(db.Boolean)

    def __init__(self, mcc_mnc, lambert93X, lambert93Y, conn_2G=False, conn_3G=False, conn_4G=False):
        self.mcc_mnc = mcc_mnc
        self.lambert93X = lambert93X
        self.lambert93Y = lambert93Y
        self.conn_2G = conn_2G
        self.conn_3G = conn_3G
        self.conn_4G = conn_4G