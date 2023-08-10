"""
Module setup logger.
"""

import logging
import os

from intel.definitions import LOG_LEVEL, NAME_PROJECT, PATH_TO_LOGS


def setup():
    """
    The function sets up and returns a logger object for writing logs to the 'logs/disobedience.log' file
    :return: the created and configured logger object
    """
    if not os.path.exists(PATH_TO_LOGS):
        os.makedirs(PATH_TO_LOGS)

    handler = logging.FileHandler(PATH_TO_LOGS + NAME_PROJECT + '.log', mode='w')
    formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s", datefmt="%H:%M:%S")
    handler.setFormatter(formatter)

    logger = logging.getLogger(NAME_PROJECT)
    logger.setLevel(LOG_LEVEL)
    logger.addHandler(handler)

    return logger
