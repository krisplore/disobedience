"""
This module provides a function for extracting the filename from command line arguments.
"""

import getopt
import logging
import sys

from intel.translation import start_translating

_ = start_translating()

py_logger12 = logging.getLogger(__name__)
py_logger12.setLevel(logging.INFO)

py_handler = logging.FileHandler(f"logs/{__name__}.log", mode='w')
py_formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

py_handler.setFormatter(py_formatter)
py_logger12.addHandler(py_handler)


def parse_filename(argv):
    """
    Extract the filename from the command line arguments.

    :param argv: A list of command line arguments.
    :type argv: list[str]
    :return: The filename extracted from the command line arguments.
    :rtype: str
    """
    py_logger12.info("parse_filename function was called")

    try:
        opts = getopt.getopt(argv, "f:", ["filename="])[0]
    except getopt.GetoptError:
        py_logger12.error("Error parsing filename option: %s", e)
        print(_("Invalid option or missing required argument"))
        sys.exit(2)

    if opts:
        py_logger12.info("Filename provided")
        filename = opts[0][1]
        return filename

    py_logger12.warning("No filename provided")
    print(_("No filename provided"))  # if admin did not enter option at all
    sys.exit(2)
