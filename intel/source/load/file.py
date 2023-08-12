"""
This module provides a function for extracting the filename from command line arguments.
"""

import getopt
import sys

from intel.definitions import ERR_DEFAULT
from intel.logger import logger
from intel.translation import setup as translation_setup

_ = translation_setup()


def parse_filename(argv):
    """
    Extract the filename from the command line arguments.

    :param argv: A list of command line arguments.
    :type argv: list[str]
    :return: The filename extracted from the command line arguments.
    :rtype: str
    """

    try:
        opts = getopt.getopt(argv, "f:", ["filename="])[0]
    except getopt.GetoptError:
        logger.error(_("Invalid option or missing required argument"))
        sys.exit(ERR_DEFAULT)

    if opts:
        logger.debug("Filename provided")
        filename = opts[0][1]
        return filename

    logger.warning(_("No filename provided"))  # if admin did not enter option at all
    sys.exit(ERR_DEFAULT)
