"""
Responsible for managing the process of adding a new source.
"""

import sys

from intel.definitions import SOURCE_EXTENSION_YAML, PATH_TO_SOURCE_MODEL, ERR_DEFAULT
from intel.log import setup
from intel.source.functions import create_stub, print_dictionary
from intel.source.load.file import parse_filename
from intel.source.load.method import parse_method_input
from intel.source.load.options import parse_options
from intel.source.validate.validator import validate
from intel.source.yaml import load, save
from intel.translation import setup as translation_setup
from intel.types.process import read

_ = translation_setup()

logger = setup()


def add():
    """
    This function handles the process of adding a new data source.
    It prompts the user for required information, generates relevant data,
    and saves it to a file.
    """
    logger.info("Add function started")
    print(_("Language"))

    model = load(PATH_TO_SOURCE_MODEL + SOURCE_EXTENSION_YAML)
    source = create_stub()
    logger.info("The stub for the source was created")

    method_input = parse_method_input()
    logger.info("Input method defined")

    match method_input:
        case 'file':
            logger.info("Case input method - file defined")
            raw_source = load(parse_filename(sys.argv[4:]))
        case 'opt':
            logger.info("Case input method - options defined")
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
        logger.info("File validation completed successfully")

        print_dictionary(result, model)
        logger.info("The result was printed")

        source.update(raw_source)
        logger.info("The raw source was merged into the stub source")

        source = read(source, model)
        logger.info("The source was sent to the read function")

        save(source, source['id'])
        logger.info("The source was written to a file")

        print_dictionary(source, model)
        logger.info("The source was printed")
