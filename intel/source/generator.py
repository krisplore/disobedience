"""
The 'options_generator' module provides a function to generate options for searching and editing based on a model.

This module contains the following function:
    - generate_options: Extracts searchable and editable options from the given model and returns them
      as dictionaries with field names as keys and corresponding short and long options as values.
"""


def generate_options(model):
    """
    The function scans the Model dictionary for the presence of the can_be_searched
    and can_be_edited fields and saves to the appropriate dictionaries.

    :param model: A dictionary representing the model containing field properties and options.
    :type: dict

    :return: two dictionaries containing searchable and editable options respectively.
    :rtype: tuple if dictionaries
    """

    searchable_options = {}
    editable_options = {}

    for field, properties in model.items():
        if 'can_be_searched' in properties and properties['can_be_searched']:
            option = properties.get('options', {})
            if 'short' in option and 'long' in option:
                searchable_options[field] = (option['short'], option['long'])

        if 'can_be_edited' in properties and properties['can_be_edited']:
            option = properties.get('options', {})
            if 'short' in option and 'long' in option:
                editable_options[field] = (option['short'], option['long'])

    return searchable_options, editable_options
