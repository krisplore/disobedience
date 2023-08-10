"""
Module provides a function for parsing input argument and retrieving the data input method.
"""

import sys

from intel.logger import setup as logger_setup

logger = logger_setup()


def parse_method_input():
    """
    Parses the input arguments and returns the data input method.

    :return: The data input method.
    :rtype: str.
    """

    way: str = sys.argv[3]
    if way:
        logger.debug("Input method defined")
    return way
