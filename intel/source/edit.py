"""
The module provides work with edit functions. Responsible for overwriting files with new values from the administrator
or user. Validates values in progress. Writes the file back to the storage.
"""
import logging
import sys

from intel.definitions import PATH_TO_SOURCE_MODEL, SOURCE_EXTENSION_YAML, PATH_TO_STORAGE
from intel.source.edit_parser import parse_edit_options
from intel.source.functions import print_dictionary, get_time
from intel.source.my_yaml import read, write
from intel.source.validate.validator import validate


py_logger3 = logging.getLogger(__name__)
py_logger3.setLevel(logging.INFO)

py_handler = logging.FileHandler(f"logs/{__name__}.log", mode='w')
py_formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

py_handler.setFormatter(py_formatter)
py_logger3.addHandler(py_handler)


def edit():
    """
    The function receives the parsed data, merges two dictionaries: old and new data, validates the received dictionary
    and overwrites the file.
    :return: None
    """
    py_logger3.info('Edit function started')

    arguments = parse_edit_options(sys.argv[3:])
    py_logger3.info('Parsed options received')

    filename = arguments['id']

    source = read(PATH_TO_STORAGE + filename + SOURCE_EXTENSION_YAML)
    py_logger3.info('Dictionary source was read')

    source['modified'] = get_time()
    py_logger3.info('Modification time set')

    source.update(arguments)
    py_logger3.info('The original dictionary merged with the new data')

    model = read(PATH_TO_SOURCE_MODEL + SOURCE_EXTENSION_YAML)
    py_logger3.info('Model source was read')

    result = validate(source, model)

    if not result['status']:
        py_logger3.error("File validation failed")
        print(result)
        sys.exit(2)

    else:
        py_logger3.info("File validation completed successfully")
        write(source, filename)
        py_logger3.info("The updated file was written")

        print_dictionary(result, model)
        py_logger3.info("The result was printed")

        print_dictionary(source, model)
        py_logger3.info("The source was printed")
