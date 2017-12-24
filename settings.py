import logging
import logging.config
import os

# Lift simulator settings
MIN_FLOW_NUM = 5             # Minimal flow number
MAX_FLOW_NUM = 20            # Maximum flow number
DEFAULT_FLOW_NUM = 9         # Default flow number
DEFAULT_FLOW_HEIGHT = 3      # Default flow height (meter)
DEFAULT_LIFT_SPEED = 1.5     # Default lift speed (meter per second)
DEFAULT_DOOR_TIME = 2        # Default time of door opening/closing (second)
DOOR_WAIT_TIMEOUT = 3        # Time while lift is wait a command with open door (second)

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


