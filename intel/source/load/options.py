"""
This module provides function for parsing command line arguments
and returns a dictionary of the parsed options.
"""

import getopt
import sys

from intel.definitions import PATH_TO_SOURCE_MODEL, SOURCE_EXTENSION_YAML
from intel.source.functions import extract_items_from_list
from intel.source.my_yaml import read
from intel.translation import start_translating

_ = start_translating()


def parse_options(argv):
    """
    Parse command line arguments.

    :param argv: A list of command line arguments.
    :type argv: list[str]

    :return: A dictionary representing the parsed options.
    :rtype: dict
    """

    map_options: dict[str, tuple[str, str]] = {
        'callsign': ('-c', '--callsign'),
        'tags': ('-t', '--tags'),
        'invited_by': ('-i', '--invited-by')
    }

    try:
        opts = getopt.getopt(argv, "c:i:t:", ["callsign=", "invited-by=", "tags="])[0]
    except getopt.GetoptError:  # invalid options - not c, i, t / if option without argument
        print(_("Invalid options or missing required arguments"))
        sys.exit(2)

    options_parsed = {}
    for opt, arg in opts:
        for key, value in map_options.items():
            if opt in value:
                options_parsed[key] = arg
                break

    extract_items_from_list(options_parsed, read(PATH_TO_SOURCE_MODEL + SOURCE_EXTENSION_YAML))

    return options_parsed
