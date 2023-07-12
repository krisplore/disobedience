"""
Provide correct work with yaml files as read, write
"""
import yaml


def read_from_yaml(filename):
    """
    Read data from a YAML file and return the parsed content.


    :param filename: The name of the YAML file to read.
    :type filename: st

    :return: The parsed data read from the YAML file
    :rtype: dict
    """
    with open(filename, 'r', encoding='utf-8') as file:
        read_data: dict = yaml.safe_load(file)
        return read_data


def save_to_yaml(source, filename):
    """
    Saves a dictionary to a YAML file.

    :param source: The dictionary to be saved.
    :type source: dict

    :param filename: The path and name of the file to save.
    :type filename: str

    :return: None
    """

    with open(filename, 'w', encoding='utf-8') as file:
        yaml.dump(source, file)
