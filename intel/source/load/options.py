"""
This module provides function for parsing command line arguments
and returns a dictionary of the parsed options.
"""

import getopt
import sys

from intel.definitions import PATH_TO_SOURCE_MODEL, SOURCE_EXTENSION_YAML, ERR_DEFAULT
from intel.logger import setup as logger_setup
from intel.source.yaml import load
from intel.translation import setup as translation_setup
from intel.types.process import read

_ = translation_setup()

logger = logger_setup()


def parse_options(argv):
    """
    Parse command line arguments.

    :param argv: A list of command line arguments.
    :type argv: list[str]

    :return: A dictionary representing the parsed options.
    :rtype: dict
    """
    logger.info("parse_options function was called")

    map_options: dict[str, tuple[str, str]] = {
        'callsign': ('-c', '--callsign'),
        'tags': ('-t', '--tags'),
        'invited_by': ('-i', '--invited-by')
    }

    try:
        opts = getopt.getopt(argv, "c:i:t:", ["callsign=", "invited-by=", "tags="])[0]
    except getopt.GetoptError as error:  # invalid options - not c, i, t / if option without argument
        logger.error("Error parsing command-line options: %s", error)
        print(_("Invalid options or missing required arguments"))
        sys.exit(ERR_DEFAULT)

    options_parsed = {}
    for opt, arg in opts:
        for key, value in map_options.items():
            if opt in value:
                options_parsed[key] = arg
                logger.info('Defined option %s and value %s in dictionary', key, arg)
                break

    options_parsed = read(options_parsed, load(PATH_TO_SOURCE_MODEL + SOURCE_EXTENSION_YAML))
    logger.info('Data type "list string separator comma" was extracted')

    return options_parsed
