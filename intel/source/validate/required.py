"""
The 'required' module provides utility function for data validation.

This module contains the following function:
    - validate_required: Check if all required fields are present in the data dictionary.
"""


def validate_required(raw_source: dict, model, result):
    """
    Check if all required fields are present in the data dictionary.

    :param raw_source: A dictionary representing the questionnaire fields and values.
    :type raw_source: dict

    :param model: A dictionary containing validation rules for each field.
    :type model: dict

    :param result: A dictionary containing the validation result.
                   The function will update the 'status' key to False and add error messages to 'errors' list
                   if any validation rules are violated.
    :type result: dict

    :return: The modified 'result' dictionary after checking for missing required fields.
    :rtype: dict
    """

    for key, rules in model.items():
        if rules.get('required', False) and key not in raw_source:
            result['status'] = False
            result['errors'].append(f'Missing argument {key}')

    return result
