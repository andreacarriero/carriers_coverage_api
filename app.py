from flask import Flask

from toolbox.logger import get_logger
from toolbox.configuration_loader import AppConfiguration
from toolbox.database import db

log = get_logger(__name__)
conf = AppConfiguration()

log.info("Starting app...")
app = Flask(__name__)

log.info("Connecting to db...")
app.config['SQLALCHEMY_DATABASE_URI'] = conf.get('databaseURI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = conf.get('databaseTrackModifications')
log.info("Connected to db")

db.init_app(app)
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(
        host = conf.get('devServerHost'),
        port = conf.get('devServerPort'),
        debug = True,
        threaded = True
    )