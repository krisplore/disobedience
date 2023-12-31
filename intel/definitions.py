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
import logging
from pathlib import Path

ERR_DEFAULT = 1
LOG_LEVEL = logging.INFO
NAME_PROJECT: str = 'disobedience'
PATH_BASE: str = str(Path(__file__).parent.parent)
PATH_TO_LOGS = PATH_BASE + '/logs/'
PATH_TO_MODELS = PATH_BASE + '/models/'
PATH_TO_MODEL_SOURCE = PATH_TO_MODELS + 'source'
PATH_TO_STORAGE: str = PATH_BASE + '/data/source/'
SOURCE_EXTENSION_YAML: str = '.yaml'
SOURCE_SCHEMA_VERSION: int = 1
