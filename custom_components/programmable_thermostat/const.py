"""Programmable thermostat's constant """
from homeassistant.components.climate import HVACMode

#Generic
VERSION = '8.3'
DOMAIN = 'programmable_thermostat'
PLATFORM = 'climate'
ISSUE_URL = 'https://github.com/custom-components/climate.programmable_thermostat/issues'
CONFIGFLOW_VERSION = 4


#Defaults
DEFAULT_TOLERANCE = 0.5
DEFAULT_NAME = 'Programmable Thermostat'
DEFAULT_MAX_TEMP = 40
DEFAULT_MIN_TEMP = 5
DEFAULT_HVAC_OPTIONS = 7
DEFAULT_FAN_OPTIONS = 3
DEFAULT_AUTO_MODE = 'all'
DEFAULT_MIN_CYCLE_DURATION = ''


#Others
MAX_HVAC_OPTIONS = 8
MAX_FAN_OPTIONS = 4
AUTO_MODE_OPTIONS = ['all', 'heating', 'cooling']
INITIAL_HVAC_MODE_OPTIONS = ['', HVACMode.COOL, HVACMode.HEAT, HVACMode.OFF, HVACMode.HEAT_COOL]
INITIAL_HVAC_MODE_OPTIONS_OPTFLOW = ['null', HVACMode.COOL, HVACMode.HEAT, HVACMode.OFF, HVACMode.HEAT_COOL]
REGEX_STRING = r'((?P<hours>\d+?):(?=(\d+?:\d+?)))?((?P<minutes>\d+?):)?((?P<seconds>\d+?))?$'

#Attributes
ATTR_HEATER_HIGH_IDS = "heater_ids"
ATTR_HEATER_MED_IDS = "heater_ids"
ATTR_HEATER_LOW_IDS = "heater_ids"
ATTR_COOLER_HIGH_IDS = "cooler_ids"
ATTR_COOLER_MED_IDS = "cooler_ids"
ATTR_COOLER_LOW_IDS = "cooler_ids"
ATTR_SENSOR_ID = "sensor_id"
