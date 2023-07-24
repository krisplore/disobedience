"""
Module to define constants and related variables.

This module contains definitions of constants and related variables.

Constants:
    PATH_BASE (str): The base path of the module,
    obtained from the parent directory of the current file.
    SOURCE_SCHEMA_VERSION: The version number of the source schema.
    EXTENSION_YAML: The file extension for YAML files.
    NAME_PROJECT: The name of the project.

Note:
    - Modifying the values of these constants is not recommended.
"""

from pathlib import Path

NAME_PROJECT: str = 'disobedience'
PATH_BASE: str = str(Path(__file__).parent.parent)
PATH_TO_SOURCE_MODEL = "intel/model_source"
SOURCE_EXTENSION_YAML: str = '.yaml'
SOURCE_SCHEMA_VERSION: int = 1
