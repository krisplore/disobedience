"""
This module provides function for parsing command line arguments
and returns a dictionary of the parsed options.
"""

import getopt
import logging
import sys

from intel.definitions import PATH_TO_SOURCE_MODEL, SOURCE_EXTENSION_YAML, ERR_BAD_OPTS
from intel.source.functions import extract_items_from_list
from intel.source.my_yaml import read
from intel.translation import start_translating

_ = start_translating()

py_logger11 = logging.getLogger(__name__)
py_logger11.setLevel(logging.INFO)

py_handler = logging.FileHandler(f"logs/{__name__}.log", mode='w')
py_formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

py_handler.setFormatter(py_formatter)
py_logger11.addHandler(py_handler)


def parse_options(argv):
    """
    Parse command line arguments.

    :param argv: A list of command line arguments.
    :type argv: list[str]

    :return: A dictionary representing the parsed options.
    :rtype: dict
    """
    py_logger11.info("parse_options function was called")

    map_options: dict[str, tuple[str, str]] = {
        'callsign': ('-c', '--callsign'),
        'tags': ('-t', '--tags'),
        'invited_by': ('-i', '--invited-by')
    }

    try:
        opts = getopt.getopt(argv, "c:i:t:", ["callsign=", "invited-by=", "tags="])[0]
    except getopt.GetoptError:  # invalid options - not c, i, t / if option without argument
        py_logger11.error("Error parsing command-line options: %s", e)
        print(_("Invalid options or missing required arguments"))
        sys.exit(ERR_BAD_OPTS)

    options_parsed = {}
    for opt, arg in opts:
        for key, value in map_options.items():
            if opt in value:
                options_parsed[key] = arg
                py_logger11.info(f'Defined option {key} and value {arg} in dictionary')
                break

    extract_items_from_list(options_parsed, read(PATH_TO_SOURCE_MODEL + SOURCE_EXTENSION_YAML))
    py_logger11.info(f'Data type "list string separator comma" was extracted')

    return options_parsed
