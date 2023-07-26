"""
This module provides a function for extracting the filename from command line arguments.
"""

import getopt
import sys

from intel.translation import start_translating

_ = start_translating()


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
