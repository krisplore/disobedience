"""
Module setup logger.
"""

import logging
import os

import colorlog

from intel.definitions import LOG_LEVEL, NAME_PROJECT, PATH_TO_LOGS

global logger

if not os.path.exists(PATH_TO_LOGS):
    os.makedirs(PATH_TO_LOGS)

handler = logging.FileHandler(PATH_TO_LOGS + NAME_PROJECT + '.log', mode='w')
formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s", datefmt="%H:%M:%S")
handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_formatter = colorlog.ColoredFormatter(
    "%(log_color)s%(levelname)s:%(name)s:%(message)s",
    datefmt="%H:%M:%S",
    log_colors={
        'DEBUG': 'green',
        'INFO': 'blue',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'red,bg_white',
    }
)

console_handler.setFormatter(console_formatter)
logger = logging.getLogger(NAME_PROJECT)
logger.setLevel(LOG_LEVEL)
logger.addHandler(handler)
logger.addHandler(console_handler)
