"""
The module provides work with edit functions. Responsible for overwriting files with new values from the administrator
or user. Validates values in progress. Writes the file back to the storage.
"""
import sys

from intel.definitions import PATH_TO_SOURCE_MODEL, SOURCE_EXTENSION_YAML, PATH_TO_STORAGE
from intel.source.edit_parser import parse_edit_options
from intel.source.functions import print_dictionary, get_time
from intel.source.my_yaml import read, write
from intel.source.validate.validator import validate


def edit():
    """
    The function receives the parsed data, merges two dictionaries: old and new data, validates the received dictionary
    and overwrites the file.
    :return: None
    """

    arguments = parse_edit_options(sys.argv[3:])

    filename = arguments['id']

    source = read(PATH_TO_STORAGE + filename + SOURCE_EXTENSION_YAML)

    source['modified'] = get_time()
    source.update(arguments)

    model = read(PATH_TO_SOURCE_MODEL + SOURCE_EXTENSION_YAML)

    result = validate(source, model)

    if not result['status']:
        print(result)
        sys.exit(2)

    else:
        write(source, filename)

        print_dictionary(result, model)
        print_dictionary(source, model)
