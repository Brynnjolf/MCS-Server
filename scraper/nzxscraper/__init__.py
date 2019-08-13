from os import path, remove
import logging
import logging.config
import json

# If applicable, delete the existing log file to generate a fresh log file during each execution
pathToLog = "/home/mcsadmin/webServer/scraper/python_logging.log"
if path.isfile(pathToLog):
    remove(pathToLog)

pathToLogConfig = "/home/mcsadmin/webServer/scraper/python_logging_configuration.json"
with open(pathToLogConfig, 'r') as logging_configuration_file:
    config_dict = json.load(logging_configuration_file)

logging.config.dictConfig(config_dict)

# Log that the logger was configured
logger = logging.getLogger(__name__)
logging.getLogger("selenium").setLevel(logging.WARNING)
logger.info('Completed configuring logger()!') 