import getopt
import sys
from intel.source.functions import extract_tags
"""
This module provides functions for parsing command line arguments.

The module includes the following functions:
- parse_options: Parses command line arguments and returns a dictionary of the parsed options.
- parse_filename: Extracts the filename from the command line arguments.
- parse_input_method: Parses the input arguments and returns the data input method.
"""


def parse_options(argv):
    """
    Parse command line arguments.

    :param argv: A list of command line arguments.
    :type argv: list[str]

    :return: A dictionary representing the parsed options.
    :rtype: dict

    """
    option_map: dict[str, tuple[str, str]] = {
        'callsign': ('-c', '--callsign'),
        'tags': ('-t', '--tags'),
        'invited by': ('-i', '--invited_by')
    }

    try:
        opts, args = getopt.getopt(argv, "c:i:t:", ["callsign=", "invited_by=", "tags="])
    except getopt.GetoptError:  # invalid options - not c, i, t / if --option without argument
        print("Invalid options or missing required arguments")
        sys.exit(2)

    parsed_options = {}
    for opt, arg in opts:
        for key, value in option_map.items():
            if opt in value:
                parsed_options[key] = arg
                break

    if parsed_options['tags']:
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
        print("Invalid options or missing required arguments")
        sys.exit(2)

    parsed_options = list((opt, arg) for opt, arg in opts)
    filename = parsed_options[0][1]

    return filename


def parse_input_method():
    """
    Parses the input arguments and returns the data input method.

    :return: The data input method.
    :rtype: str.
    """

    way: str = sys.argv[3]

    return way
