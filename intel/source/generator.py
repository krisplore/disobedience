"""
The 'options_generator' module provides a function to generate options for searching and editing based on a model.

This module contains the following function:
    - generate_options: Extracts searchable and editable options from the given model and returns them
      as list with options as values.
"""

from intel.log import setup

logger = setup()


def generate_options(model):
    """
    The function scans the Model dictionary for the presence of the can_be_searched
    and can_be_edited fields and saves to the appropriate list.

    :param model: A dictionary representing the model containing field properties and options.
    :type: dict

    :return: List of command line options.
    :rtype: List
    """
    logger.info("generate_options function was called")

    searchable_options = {}
    editable_options = {}

    for field, properties in model.items():
        if 'can_be_searched' in properties and properties['can_be_searched']:
            option = properties.get('option', {})
            searchable_options[field] = 'where.' + option + '='
            logger.info("Added searchable option: %s", searchable_options[field])

        if 'can_be_edited' in properties and properties['can_be_edited']:
            option = properties.get('option', {})
            editable_options[field] = 'new.' + option + '='
            logger.info("Added editable option: %s", editable_options[field])

    options = searchable_options.copy()
    options.update(editable_options)
    options = list(options.values())

    return options
