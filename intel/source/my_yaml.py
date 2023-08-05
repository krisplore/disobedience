"""
This module provides functions for working with YAML files.

The module includes the following functions:
- read: Reads data from a YAML file and returns the parsed content.
- write: Saves a dictionary to a YAML file.
"""
import logging

import yaml
from intel.definitions import SOURCE_EXTENSION_YAML, PATH_BASE

PATH_TO_STORAGE: str = PATH_BASE + '/data/source/'

py_logger10 = logging.getLogger(__name__)
py_logger10.setLevel(logging.INFO)

py_handler = logging.FileHandler(f"logs/{__name__}.log", mode='w')
py_formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

py_handler.setFormatter(py_formatter)
py_logger10.addHandler(py_handler)


def read(filename):
    """
    Reads data from a YAML file and returns the parsed content.

    :param filename: The name of the YAML file to read.
    :type filename: str

    :return: A dictionary representing the parsed content from the YAML file.
    :rtype: dict
    """
    py_logger10.info("read function was called")

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            file_parsed: dict = yaml.safe_load(file)
            py_logger10.info("File '%s' successfully read.", filename)
            return file_parsed
    except FileNotFoundError as e:
        py_logger10.error("File not found: %s", filename)
        raise e
    except yaml.YAMLError as e:
        py_logger10.error("Error parsing the YAML file '%s': %s", filename, e)
        raise e


def write(dictionary, filename):
    """
    Saves a dictionary to a YAML file.

    :param dictionary: The dictionary to be saved.
    :type dictionary: dict

    :param filename: The name of the file to save.
    :type filename: str

    :return: None
    """
    py_logger10.info("write function was called")

    try:
        with open(PATH_TO_STORAGE + filename + SOURCE_EXTENSION_YAML, 'w', encoding='utf-8') as file:
            yaml.dump(dictionary, file)
        py_logger10.info("Dictionary successfully written to file '%s'.", filename + SOURCE_EXTENSION_YAML)
    except Exception as e:
        py_logger10.error("Error writing dictionary to file '%s': %s", filename + SOURCE_EXTENSION_YAML, e)
        raise e
