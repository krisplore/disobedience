"""
This module provides function for parsing command line arguments
and returns a dictionary of the parsed options.
"""

import getopt
import sys
from intel.translation import start_translating
from intel.source.functions import extract_tags

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
        'invited by': ('-i', '--invited-by')
    }

    try:
        opts, args = getopt.getopt(argv, "c:i:t:", ["callsign=", "invited-by=", "tags="])
    except getopt.GetoptError:  # invalid options - not c, i, t / if option without argument
        print(_("Invalid options or missing required arguments"))
        sys.exit(2)

    options_parsed = {}
    for opt, arg in opts:
        for key, value in map_options.items():
            if opt in value:
                options_parsed[key] = arg
                break

    if 'tags' in options_parsed:
        options_parsed['tags'] = extract_tags(options_parsed['tags'])

    return options_parsed
