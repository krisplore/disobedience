"""
The module is responsible for the function that retrieves the values for the options to edit the file.
"""

import getopt
import logging
import sys

from intel.definitions import PATH_TO_SOURCE_MODEL, SOURCE_EXTENSION_YAML, ERR_BAD_OPTS
from intel.source.functions import extract_items_from_list, replace_hyphen_with_underscore
from intel.source.generator import generate_options
from intel.source.my_yaml import read
from intel.translation import start_translating

_ = start_translating()

py_logger4 = logging.getLogger(__name__)
py_logger4.setLevel(logging.INFO)

py_handler = logging.FileHandler(f"logs/{__name__}.log", mode='w')
py_formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

py_handler.setFormatter(py_formatter)
py_logger4.addHandler(py_handler)


def parse_edit_options(argv):
    """
    The function parses the options and values of the command line, to obtain the option
    where. - source file qualifier and new. - data to change.

    :param argv: command line value
    :return: a dictionary from command line values
    :rtype: dict
    """
    py_logger4.info('Parse_edit_options function started')
    model = read(PATH_TO_SOURCE_MODEL + SOURCE_EXTENSION_YAML)
    options = generate_options(model)

    try:
        opts = getopt.getopt(argv, '', options)[0]
        py_logger4.info('Command line options processed successfully')
    except getopt.GetoptError as err:
        py_logger4.error(f"Error raised while parsing options: {str(err)}")
        print(str(err))
        sys.exit(ERR_BAD_OPTS)

    new_values = {}
    for opt, arg in opts:
        if '--where' in opt:
            key = opt.split('.')[-1]
            new_values[key] = arg
            py_logger4.info(f'Defined option {key} and value {arg} in dictionary')

        elif '--new' in opt:
            key = opt.split('.')[-1]
            key = replace_hyphen_with_underscore(key)
            new_values[key] = arg
            py_logger4.info(f'Defined option {key} and value {arg} in dictionary')

    extract_items_from_list(new_values, model)
    py_logger4.info(f'Data type "list string separator comma" was extracted')

    return new_values
