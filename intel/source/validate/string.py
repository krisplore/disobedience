"""
The string module provides a function to validate the string data type.

This module contains the following function:
    - validate_length_string: Check if the length of specified fields in the data dictionary
    meets the validation rules.
"""

from intel.log import logger_setup

logger = logger_setup()


def validate_length_string(raw_source: dict, model: dict, result: dict):
    """
    The function compares the received values with the data from the model, which represents the set of rules
    for the dictionary.

    :param raw_source: dictionary with data to be checked
    :param model: dict of rules
    :param result: dictionary with the results of the check
    :return: dictionary with the results of the check
    """

    logger.info("validate_length_string function was called")

    for field, properties in model.items():
        if 'type' in properties and properties['type'] == 'string' and 'length' in properties:
            min_length = properties['length'].get('min')
            max_length = properties['length'].get('max')

            if field in raw_source:
                value = raw_source[field]
                if isinstance(value, str):
                    if min_length is not None and len(value) < min_length:
                        result['status'] = False
                        result['errors'].append(f'The length of the {field} must be at least {min_length} characters')

                        logger.warning("Invalid length for '%s'. Length must be at least %s "
                                       "characters.", field, min_length)

                    if max_length is not None and len(value) > max_length:
                        result['status'] = False
                        result['errors'].append(f'The length of the {field} must be at most {max_length} characters')

                        logger.warning("Invalid length for '%s'. Length must be at most %s "
                                       "characters.", field, max_length)

    return result
