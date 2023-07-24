"""
Module 'model' for creating and saving dictionaries to YAML files.

This module provides functions to create dictionaries representing data models and save them to YAML files.
The data models are used for validating and comparing input data.
"""

import yaml
from intel.definitions import SOURCE_EXTENSION_YAML

model_source = {
    'callsign': {
        'required': True,
        'min length': 2,
        'max length': 16
    },
    'invited by': {
        'required': True
    },
    'tags': {
        'required': False
    }
}

with open('model_source' + SOURCE_EXTENSION_YAML, 'w', encoding='utf-8') as file:
    yaml.dump(model_source, file)
