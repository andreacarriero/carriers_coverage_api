from flask_restful import Resource, reqparse, abort

from toolbox.logger import get_logger
from models.carriers import Carrier, CarrierConnectivity
from modules.address_api import AddressApiParserFR, RequestError, BadRequestError, NoResultsError

log = get_logger(__name__)
address_api_parser_fr = AddressApiParserFR()

class LocationResource(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('q', type=str, required=True)
        args = parser.parse_args()

        try:
            location = address_api_parser_fr.search(args['q'])       
        except RequestError as e:
            return {
                'message': str(e)
            }, 500
        except (BadRequestError, NoResultsError) as e:
            return {
                'message': str(e)
            }, 400
        except Exception as e:
            abort(500)

        return {
            'meta': {
                'location': location
            }
        }
