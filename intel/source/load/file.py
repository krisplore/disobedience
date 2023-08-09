"""
This module provides a function for extracting the filename from command line arguments.
"""

import getopt
import sys

from intel.definitions import ERR_DEFAULT
from intel.logger import setup as logger_setup
from intel.translation import setup as translation_setup

_ = translation_setup()

logger = logger_setup()


def parse_filename(argv):
    """
    Extract the filename from the command line arguments.

    :param argv: A list of command line arguments.
    :type argv: list[str]
    :return: The filename extracted from the command line arguments.
    :rtype: str
    """
    logger.info("parse_filename function was called")

    try:
        opts = getopt.getopt(argv, "f:", ["filename="])[0]
    except getopt.GetoptError as error:
        logger.error("Error parsing filename option: %s", error)
        print(_("Invalid option or missing required argument"))
        sys.exit(ERR_DEFAULT)

    if opts:
        logger.info("Filename provided")
        filename = opts[0][1]
        return filename

    logger.warning("No filename provided")
    print(_("No filename provided"))  # if admin did not enter option at all
    sys.exit(ERR_DEFAULT)
