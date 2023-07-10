"""
Module to define constants and related variables.

This module contains definitions of constants and related variables.

Constants:
    PATH_BASE (str): The base path of the module,
    obtained from the parent directory of the current file.
    SOURCE_SCHEMA_VERSION: The version number of the source schema.

Note:
    - Modifying the values of these constants is not recommended.
"""

from pathlib import Path

PATH_BASE: str = str(Path(__file__).parent.parent)
SOURCE_SCHEMA_VERSION = 1
