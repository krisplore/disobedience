"""
This module provides functions for working with YAML files.

The module includes the following functions:
- read_from_yaml: Reads data from a YAML file and returns the parsed content.
- save_to_yaml: Saves a dictionary to a YAML file.
"""
import yaml


def read_from_yaml(filename):
    """
    Reads data from a YAML file and returns the parsed content.

    :param filename: The name of the YAML file to read.
    :type filename: str
    :return: A dictionary representing the parsed content from the YAML file.
    :rtype: dict
    """

    with open(filename, 'r', encoding='utf-8') as file:
        parsed_file: dict = yaml.safe_load(file)

        return parsed_file


def save_to_yaml(dictionary, filename):
    """
    Saves a dictionary to a YAML file.

    :param dictionary: The dictionary to be saved.
    :type dictionary: dict

    :param filename: The path and name of the file to save.
    :type filename: str

    :return: None
    """

    with open(filename, 'w', encoding='utf-8') as file:
        yaml.dump(dictionary, file)
