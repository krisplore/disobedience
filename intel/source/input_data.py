"""
This module provides functions for parsing command line arguments.

The module includes the following functions:
- parse_options: Parses command line arguments and returns a dictionary of the parsed options.
- parse_filename: Extracts the filename from the command line arguments.
- parse_input_method: Parses the input arguments and returns the data input method.
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

    parsed_options = {}
    for opt, arg in opts:
        for key, value in map_options.items():
            if opt in value:
                parsed_options[key] = arg
                break

    if 'tags' in parsed_options:
        parsed_options['tags'] = extract_tags(parsed_options['tags'])

    return parsed_options


def parse_filename(argv):
    """
    Extract the filename from the command line arguments.

    :param argv: A list of command line arguments.
    :type argv: list[str]
    :return: The filename extracted from the command line arguments.
    :rtype: str
    """

    try:
        opts, args = getopt.getopt(argv, "f:", ["filename="])
    except getopt.GetoptError:
        print(_("Invalid option or missing required argument"))
        sys.exit(2)

    if opts:
        filename = opts[0][1]
        return filename
    print(_("No filename provided"))  # if admin did not enter option at all
    sys.exit(2)


def parse_method_input():
    """
    Parses the input arguments and returns the data input method.

    :return: The data input method.
    :rtype: str.
    """

    way: str = sys.argv[3]

    return way
