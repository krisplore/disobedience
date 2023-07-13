"""
This module provides a function to translate strings that are printed to the user.

The module includes the following function:
- start_translating: A function that initializes the translation module and returns a translation function.

The translation function returned by start_translating can be used throughout the program
to translate strings into the user's preferred language.
"""

import gettext
from intel.definitions import NAME_PROJECT, PATH_BASE

PATH_TO_LOCALES: str = PATH_BASE + '/locales'


def start_translating():
    """
    Initialize the translation module and return a translation function.

    :return: A function that can be used to translate strings into the user's preferred language.
    :rtype: function
    """

    language = gettext.translation(NAME_PROJECT, localedir=PATH_TO_LOCALES)
    language.install()
    translate = language.gettext

    return translate
