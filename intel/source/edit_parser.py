"""
The module is responsible for the function that retrieves the values for the options to edit the file.
"""

import getopt
import sys

from intel.definitions import PATH_TO_SOURCE_MODEL, SOURCE_EXTENSION_YAML
from intel.source.functions import extract_items_from_list, replace_hyphen_with_underscore
from intel.source.generator import generate_options
from intel.source.my_yaml import read


def parse_edit_options(argv):
    """
    The function parses the options and values of the command line, to obtain the option
    where. - source file qualifier and new. - data to change.

    :param argv: command line value
    :return: a dictionary from command line values
    :rtype: dict
    """
    model = read(PATH_TO_SOURCE_MODEL + SOURCE_EXTENSION_YAML)
    options = generate_options(model)

    try:
        opts = getopt.getopt(argv, '', options)[0]
    except getopt.GetoptError as err:
        print(str(err))
        sys.exit(2)

    new_values = {}
    for opt, arg in opts:
        if '--where' in opt:
            key = opt.split('.')[-1]
            new_values[key] = arg
        elif '--new' in opt:
            key = opt.split('.')[-1]
            key = replace_hyphen_with_underscore(key)
            new_values[key] = arg

    extract_items_from_list(new_values, model)


    return new_values
