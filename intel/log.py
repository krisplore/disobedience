"""
Module setup logger.
"""

import logging
import os

from intel.definitions import LOG_LEVEL


def setup_logger():
    """
    The function sets up and returns a logger object for writing logs to the 'logs/disobedience.log' file
    :return: the created and configured logger object
    """
    if not os.path.exists('logs'):
        os.makedirs('logs')

    handler = logging.FileHandler('logs/disobedience.log', mode='w')
    formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
    handler.setFormatter(formatter)

    logger = logging.getLogger('disobedience')
    logger.setLevel(LOG_LEVEL)
    logger.addHandler(handler)

    return logger
