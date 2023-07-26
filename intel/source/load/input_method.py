"""
Module provides a function for parsing input argument and retrieving the data input method.
"""

import sys


def parse_method_input():
    """
    Parses the input arguments and returns the data input method.

    :return: The data input method.
    :rtype: str.
    """

    way: str = sys.argv[3]

    return way
