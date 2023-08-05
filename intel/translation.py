"""
This module provides a function to translate strings that are printed to the user.

The module includes the following function:
- start_translating: A function that initializes the translation module and returns a translation function.

The translation function returned by start_translating can be used throughout the program
to translate strings into the user's preferred language.
"""

import gettext
import logging

from intel.definitions import NAME_PROJECT, PATH_BASE

PATH_TO_LOCALES: str = PATH_BASE + '/locales'


py_logger9 = logging.getLogger(__name__)
py_logger9.setLevel(logging.INFO)

py_handler = logging.FileHandler(f"logs/{__name__}.log", mode='w')
py_formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

py_handler.setFormatter(py_formatter)
py_logger9.addHandler(py_handler)


def start_translating():
    """
    Initialize the translation module and return a translation function.

    :return: A function that can be used to translate strings into the user's preferred language.
    :rtype: function
    """
    py_logger9.info("start_translating function was called")

    language = gettext.translation(NAME_PROJECT, localedir=PATH_TO_LOCALES)

    try:
        language.install()
        py_logger9.info("Translation language installed successfully.")
    except FileNotFoundError as err:
        py_logger9.error("Failed to install translation language: %s", err)
    translate = language.gettext

    return translate
