"""
The module provides work with edit functions. Responsible for overwriting files with new values from the administrator
or user. Validates values in progress. Writes the file back to the storage.
"""

import sys

from intel.definitions import PATH_TO_SOURCE_MODEL, SOURCE_EXTENSION_YAML, PATH_TO_STORAGE, ERR_DEFAULT
from intel.logging import setup as logging_setup
from intel.source.edit_parser import parse_edit_options
from intel.source.functions import print_dictionary, get_time
from intel.source.yaml import load, save
from intel.source.validate.validator import validate
from intel.types.process import read

logger = logging_setup()


def edit():
    """
    The function receives the parsed data, merges two dictionaries: old and new data, validates the received dictionary
    and overwrites the file.
    :return: None
    """
    logger.info('Edit function started')

    arguments = parse_edit_options(sys.argv[3:])
    logger.info('Parsed options received')

    filename = arguments['id']

    source = load(PATH_TO_STORAGE + filename + SOURCE_EXTENSION_YAML)
    logger.info('Dictionary source was read')

    source['modified'] = get_time()
    logger.info('Modification time set')

    source.update(arguments)
    logger.info('The original dictionary merged with the new data')

    model = load(PATH_TO_SOURCE_MODEL + SOURCE_EXTENSION_YAML)
    logger.info('Model source was read')

    result = validate(source, model)

    if not result['status']:
        logger.error("File validation failed")
        print(result)
        sys.exit(ERR_DEFAULT)

    else:
        logger.info("File validation completed successfully")

        source = read(source, model)
        logger.info("The source was sent to the read function")

        save(source, filename)
        logger.info("The updated source was written")

        print_dictionary(result, model)
        logger.info("The result was printed")

        print_dictionary(source, model)
        logger.info("The source was printed")
