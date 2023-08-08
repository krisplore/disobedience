"""
The module is responsible for the function that retrieves the values for the options to edit the file.
"""

import getopt
import sys

from intel.definitions import PATH_TO_SOURCE_MODEL, SOURCE_EXTENSION_YAML, ERR_DEFAULT
from intel.log import setup_logger
from intel.source.functions import sync_name
from intel.source.generator import generate_options
from intel.source.yaml import load
from intel.translation import start_translating

_ = start_translating()

logger = setup_logger()


def parse_edit_options(argv):
    """
    The function parses the options and values of the command line, to obtain the option
    where. - source file qualifier and new. - data to change.

    :param argv: command line value
    :return: a dictionary from command line values
    :rtype: dict
    """
    logger.info('Parse_edit_options function started')
    model = read(PATH_TO_SOURCE_MODEL + SOURCE_EXTENSION_YAML)
    options = generate_options(model)

    try:
        opts = getopt.getopt(argv, '', options)[0]
        logger.info('Command line options processed successfully')
    except getopt.GetoptError as err:
        logger.error("Error raised while parsing options: %s", str(err))
        print(str(err))
        sys.exit(ERR_DEFAULT)

    new_values = {}
    for opt, arg in opts:
        if '--where' in opt:
            key = opt.split('.')[-1]
            new_values[key] = arg
            logger.info('Defined option %s and value %s in dictionary', key, arg)

        elif '--new' in opt:
            key = opt.split('.')[-1]
            key = synch_name(key)
            new_values[key] = arg
            logger.info('Defined option %s and value %s in dictionary', key, arg)

    extract_items_from_list(new_values, model)
    logger.info('Data type "list string separator comma" was extracted')

    return new_values
