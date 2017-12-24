import logging
import logging.config
import os

# Lift simulator settings
MIN_FLOOR_NUM = 5             # Minimal floor number
MAX_FLOOR_NUM = 20            # Maximum floor number

MIN_FLOOR_HEIGHT = 2.0        # Minimal floor height
MAX_FLOOR_HEIGHT = 10.0       # Maximum floor height

MIN_LIFT_SPEED = 0.1          # Minimal lift speed
MAX_LIFT_SPEED = 5.0          # Maximum lift speed

MIN_DOOR_TIME = 0.1           # Minimal door opening/closing time
MAX_DOOR_TIME = 10.0          # Maximum door opening/closing time


DEFAULT_FLOOR_NUM = 9         # Default floor number
DEFAULT_FLOOR_HEIGHT = 3.0    # Default floor height (meter)
DEFAULT_LIFT_SPEED = 1.5      # Default lift speed (meter per second)
DEFAULT_DOOR_TIME = 2.0       # Default time of door opening/closing (second)
DOOR_WAIT_TIMEOUT = 3.0       # Time while lift is wait a command with open door (second)

# Logger settings
BASE_LOGGER = 'app_server_mb'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'base': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'base',
        },
    },
    'loggers': {
        BASE_LOGGER: {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    },
    'root': {
        'level': 'ERROR',
        'handlers': ['console'],
    }
}

LOGGING_LEVEL = int(os.environ.get('PYTHONLOGGINLEVEL', logging.DEBUG))


def setup_logging(base_severity=LOGGING_LEVEL):
    """
    This method configure logger

    :param int base_severity: logging level

    :return log: configured logger instance
    :rtype: logging.Logger
    """
    logging.config.dictConfig(LOGGING)
    log = logging.getLogger(BASE_LOGGER)
    log.setLevel(base_severity)

    return log


logger = setup_logging()


