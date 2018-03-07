import requests, json

from toolbox.logger import get_logger
from toolbox.configuration_loader import AppConfiguration

log = get_logger(__name__)
conf = AppConfiguration()

class RequestError(Exception):
    def __init__(self, message):
        self.message = message

class BadRequestError(Exception):
    def __init__(self, message):
        self.message = message

class NoResultsError(Exception):
    def __init__(self, message):
        self.message = message

class AddressAPIProviderError(Exception):
    def __init__(self, message):
        self.message = message

class LocationResponse():
    def __init__(self, label, context, city, coord_x, coord_y):
        self.label = label
        self.context = context
        self.city = city
        self.coord_x = coord_x
        self.coord_y = coord_y

    def serialize(self):
        return {
            'lable': self.label,
            'context': self.context,
            'city': self.city,
            'coordinates': {
                'x': self.coord_x,
                'y': self.coord_y
            }
        }

class AddressApiParserFR():
    def __init__(self):
        self.api_endpoint = conf.get('franceAddressAPIEndpoint')

    def search(self, address):
        query_string = {
            'q': address
        }
        
        headers = {
            'Cache-Control': "no-cache"
        }

        url = self.api_endpoint + '/search'
        response = requests.request("GET", url, headers=headers, params=query_string)
        
        if response.status_code == 200:
            jresponse = json.loads(response.text)

            try:
                if len(jresponse['features']) == 0:
                    log.error('No results with q: %s' % address)
                    raise NoResultsError("No results. Please change your search terms.")

                selected_jresponse = jresponse['features'][0]
                location_response = LocationResponse(
                    selected_jresponse['properties']['label'],
                    selected_jresponse['properties']['context'],
                    selected_jresponse['properties']['city'],
                    selected_jresponse['geometry']['coordinates'][0],
                    selected_jresponse['geometry']['coordinates'][1]
                )
            except KeyError as e:
                log.error('Address API provider error: %s' % e)
                raise AddressAPIProviderError('Error when parsing location provider API')

            return location_response.serialize()

        elif response.status_code == 400:
            log.error('Bad request with q: %s' % address)
            raise BadRequestError("Bad request. Details: %s" % response.text)
        else:
            log.error('Request error with q: %s' % address)
            raise RequestError("Response status code: %s. Response content: %s" % (response.status_code, response.text))
