from flask_restful import Resource, reqparse, abort

from toolbox.logger import get_logger
from toolbox.configuration_loader import AppConfiguration
from models.carriers import Carrier, CarrierConnectivity, get_connectivity_in_city
from modules.address_api import AddressApiParserFR, RequestError, BadRequestError, NoResultsError

log = get_logger(__name__)
conf = AppConfiguration()
address_api_parser_fr = AddressApiParserFR()

class LocationResource(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('q', type=str, required=True)
        parser.add_argument('all', type=bool, default=False, store_missing=True)
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

        connectivity_in_city = get_connectivity_in_city(location['city'])

        response = {
            'meta': {
                'location': location
            }
        }

        if args['all']:
            response.update(connectivity_in_city)
        else:
            carriers_to_show = conf.get('carriersToShow')
            for carrier in connectivity_in_city:
                if carrier in carriers_to_show:
                    response.update({carrier: connectivity_in_city[carrier]})

        return response
