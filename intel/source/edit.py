"""
The module provides work with edit functions. Responsible for overwriting files with new values from the administrator
or user. Validates values in progress. Writes the file back to the storage.
"""

import sys

from intel.definitions import PATH_TO_SOURCE_MODEL, SOURCE_EXTENSION_YAML, PATH_TO_STORAGE
from intel.log import setup_logger
from intel.source.edit_parser import parse_edit_options
from intel.source.functions import print_dictionary, get_time
from intel.source.yaml import load, save
from intel.source.validate.validator import validate


logger = setup_logger()


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

    source = read(PATH_TO_STORAGE + filename + SOURCE_EXTENSION_YAML)
    logger.info('Dictionary source was read')

    source['modified'] = get_time()
    logger.info('Modification time set')

    source.update(arguments)
    logger.info('The original dictionary merged with the new data')

    model = read(PATH_TO_SOURCE_MODEL + SOURCE_EXTENSION_YAML)
    logger.info('Model source was read')

    result = validate(source, model)

    if not result['status']:
        logger.error("File validation failed")
        print(result)
        sys.exit(2)

    else:
        logger.info("File validation completed successfully")
        write(source, filename)
        logger.info("The updated file was written")

        print_dictionary(result, model)
        logger.info("The result was printed")

        print_dictionary(source, model)
        logger.info("The source was printed")
