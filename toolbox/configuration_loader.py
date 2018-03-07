import json

from toolbox.logger import get_logger

log = get_logger(__name__)

class AppConfiguration():
    """
    Example
    =======
    ```
    from toolbox.configuration_loader import AppConfiguration
    conf = AppConfuguration()
    ip = conf.get('ip')
    ```
    """
    
    CONFIGURATION_FILE_PATH = 'data/configuration.json'

    def __init__(self):
        try:
            log.info("Loading configuration file...")
            with open(self.CONFIGURATION_FILE_PATH) as configuration_file:
                self.jconf = json.load(configuration_file)
        except Exception as e:
            log.error("Something is wrong with the root configuration file.\n%s" % e)
    
    def get(self, key):
        return self.jconf[key]