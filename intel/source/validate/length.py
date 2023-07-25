"""
The 'length' module provides utility functions for data validation.

This module contains the following function:
    - validate_length: Check if the length of specified fields in the data dictionary meets the validation rules.

Note: This module is designed for use with Python 3.x.
"""


def validate_length(raw_source, model, result):
    """
    Check if the length of specified fields in the data dictionary meets the validation rules.

    :param raw_source: A dictionary representing the questionnaire fields and values.
    :type raw_source: dict

    :param model: A dictionary containing validation rules for each field.
    :type model: dict

    :param result: A dictionary containing the validation result.
                   The function will update the 'status' key to False and add error messages to 'errors' list
                   if any validation rules are violated.
    :type result: dict

    :return: The modified 'result' dictionary after checking the length of specified fields.
    :rtype: dict
    """

    for key, rules in model.items():
        if key in raw_source:
            value = raw_source[key]

            if 'min length' in rules and len(value) < rules['min length']:
                result['status'] = False
                result['errors'].append(f'The length of the {key} must be between 2 and 16 characters')

            if 'max length' in rules and len(value) > rules['max length']:
                result['status'] = False
                result['errors'].append(f'The length of the {key} must be between 2 and 16 characters')

    return result
