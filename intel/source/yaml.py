"""
This module provides functions for working with YAML files.

The module includes the following functions:
- read: Reads data from a YAML file and returns the parsed content.
- write: Saves a dictionary to a YAML file.
"""

import yaml
from intel.definitions import SOURCE_EXTENSION_YAML, PATH_BASE
from intel.log import setup_logger

PATH_TO_STORAGE: str = PATH_BASE + '/data/source/'

logger = setup_logger()


def read(filename):
    """
    Reads data from a YAML file and returns the parsed content.

    :param filename: The name of the YAML file to read.
    :type filename: str

    :return: A dictionary representing the parsed content from the YAML file.
    :rtype: dict
    """
    logger.info("read function was called")

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            file_parsed: dict = yaml.safe_load(file)
            logger.info("File '%s' successfully read.", filename)
            return file_parsed
    except FileNotFoundError as error:
        logger.error("File not found: %s", filename)
        raise error
    except yaml.YAMLError as error:
        logger.error("Error parsing the YAML file '%s': %s", filename, error)
        raise error


def save(dictionary, filename):
    """
    Saves a dictionary to a YAML file.

    :param dictionary: The dictionary to be saved.
    :type dictionary: dict

    :param filename: The name of the file to save.
    :type filename: str

    :return: None
    """
    logger.info("write function was called")

    try:
        with open(PATH_TO_STORAGE + filename + SOURCE_EXTENSION_YAML, 'w', encoding='utf-8') as file:
            yaml.dump(dictionary, file)
        logger.info("Dictionary successfully written to file '%s'.", filename + SOURCE_EXTENSION_YAML)
    except Exception as error:
        logger.error("Error writing dictionary to file '%s': %s", filename + SOURCE_EXTENSION_YAML, error)
        raise error
