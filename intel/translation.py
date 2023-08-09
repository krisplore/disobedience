"""
This module provides a function to translate strings that are printed to the user.

The module includes the following function:
- start_translating: A function that initializes the translation module and returns a translation function.

The translation function returned by start_translating can be used throughout the program
to translate strings into the user's preferred language.
"""

import gettext
from intel.definitions import NAME_PROJECT, PATH_BASE
from intel.log import logger_setup

PATH_TO_LOCALES: str = PATH_BASE + '/locales'


logger = logger_setup()


def start_translating():
    """
    Initialize the translation module and return a translation function.

    :return: A function that can be used to translate strings into the user's preferred language.
    :rtype: function
    """
    logger.info("start_translating function was called")

    language = gettext.translation(NAME_PROJECT, localedir=PATH_TO_LOCALES)

    try:
        language.install()
        logger.info("Translation language installed successfully.")
    except FileNotFoundError as err:
        logger.error("Failed to install translation language: %s", err)
    translate = language.gettext

    return translate
