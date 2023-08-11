"""
The module provides 2 functions for reading and writing information to the screen for the user
and to a file for the program.

The functions determine the data type and sends the information to the next function.
"""

from intel.logger import logger
from intel.types.list_as_string import las_read, las_write


def read(data, model):
    """
    Responsible for block reading information from the screen into a file.

    :param data: dictionary to be read in correct format
    :param model: dictionary with rules for data
    :return: correctly read information
    """
    for field, properties in model.items():
        field_type = properties.get('type')
        if field in data:
            value = data.get(field)
            match field_type:
                case 'list_as_string':
                    data[field] = las_read(value, properties)
                    logger.debug('Case match %s and "list_as_string" in read function', field_type)

    return data


def write(data, model):
    """
    The function responsible for the block of writing information from the file
    to the screen in a human-readable format.

    :param data: dictionary to be written in correct format
    :param model: dictionary with rules for data
    :return: correct written information
    """
    for field, properties in model.items():
        field_type = properties.get('type')
        if field in data:
            value = data.get(field)
            match field_type:
                case 'list_as_string':
                    data[field] = las_write(value, properties)
                    logger.debug('Case match %s and "list_as_string" in write function', field_type)

    return data
