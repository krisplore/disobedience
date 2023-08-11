"""
The module is responsible for converting information into the desired format.
"""
from intel.logger import setup as logger_setup

logger = logger_setup()


def las_read(value, properties):
    """
    The function splits the value by the separator from a string and writes it to the list.

    :param value: value to be changed
    :param properties: the rules by which the value changes
    :return: correctly written value
    """
    separator = properties.get('separator', ',')
    if isinstance(value, str):
        value = [item.strip() for item in value.split(separator) if item.strip()]
        logger.debug('Data type "list_as_string" was written to list')
    return value


def las_write(value: list, properties):
    """
    The function joins a string by the separator from the list.

    :param value: value to be changed
    :param properties: the rules by which the value changes
    :return: correctly written value
    """
    separator = properties.get('separator', ',')
    if isinstance(value, list):
        separator += " "
        value = separator.join(value)
        logger.debug('Data type "list_as_string" was written to string')

    return value


def validate():
    pass
