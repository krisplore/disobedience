"""
Module provides a function for parsing input argument and retrieving the data input method.
"""
import logging
import sys

py_logger13 = logging.getLogger(__name__)
py_logger13.setLevel(logging.INFO)

py_handler = logging.FileHandler(f"logs/{__name__}.log", mode='w')
py_formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

py_handler.setFormatter(py_formatter)
py_logger13.addHandler(py_handler)


def parse_method_input():
    """
    Parses the input arguments and returns the data input method.

    :return: The data input method.
    :rtype: str.
    """
    py_logger13.info("parse_method_input function was called")

    way: str = sys.argv[3]

    return way
