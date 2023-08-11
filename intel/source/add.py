"""
Responsible for managing the process of adding a new source.
"""

import sys

from intel.definitions import (ERR_DEFAULT, PATH_TO_MODEL_SOURCE,
                               SOURCE_EXTENSION_YAML)
from intel.logger import logger
from intel.source.functions import create_stub, print_dictionary
from intel.source.load.file import parse_filename
from intel.source.load.method import parse_method_input
from intel.source.load.options import parse_options
from intel.source.validate.validator import validate
from intel.source.yaml import load, save
from intel.translation import setup as translation_setup
from intel.types.process import read

_ = translation_setup()


def add():
    """
    This function handles the process of adding a new data source.
    It prompts the user for required information, generates relevant data,
    and saves it to a file.
    """

    model = load(PATH_TO_MODEL_SOURCE + SOURCE_EXTENSION_YAML)
    source = create_stub()
    if source:
        logger.debug("The stub for the source was created")

    method_input = parse_method_input()

    match method_input:
        case 'file':
            logger.debug("Case input method - file defined")
            raw_source = load(parse_filename(sys.argv[4:]))
        case 'opt':
            logger.debug("Case input method - options defined")
            raw_source = parse_options(sys.argv[4:])
        case _:
            logger.error("Case input method not defined")
            print(_('Method does not exist'))
            sys.exit(ERR_DEFAULT)

    result = validate(raw_source, model)

    if not result['status']:
        logger.error("File validation failed")
        print(result)
        sys.exit(ERR_DEFAULT)
    else:
        logger.debug("File validation completed successfully")

        print_dictionary(result, model)

        source.update(raw_source)

        source = read(source, model)

        save(source, source['id'])

        print_dictionary(source, model)
