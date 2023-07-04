"""
Provide correct work with yaml files as read, write
"""
import yaml


def save_to_yaml(source, filename):
    """
    Saves the 'source' dictionary to a YAML file.

    :param source: The dictionary to be saved.
    :type source: dict

    :param filename: The path and name of the file to save.
    :type filename: str

    :return: None
    """
    with open(filename, 'w') as file:
        yaml.dump(source, file)


