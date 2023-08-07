"""
Module provides a function for parsing input argument and retrieving the data input method.
"""

import sys
from intel.log import setup_logger

logger = setup_logger()


def parse_method_input():
    """
    Parses the input arguments and returns the data input method.

    :return: The data input method.
    :rtype: str.
    """
    logger.info("parse_method_input function was called")

    way: str = sys.argv[3]

    return way
