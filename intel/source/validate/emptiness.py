"""
The 'empty_string' module provides utility function for data validation.

This module contains the following function:
    - validate_emptiness: Check if the values in the data dictionary are not None, not empty strings,
    and not containing only whitespace.
"""


def validate_empty_string(raw_source: dict, model: dict, result: dict):
    """
    Check if the values in the data dictionary are not None,
    not empty strings, and not containing only whitespace.

    If a required field value is None, empty, or contains only whitespace,
    the function updates the 'status' key in the 'result' dictionary to False
    and adds an error message to the 'errors' list.

    :param raw_source: A dictionary representing the questionnaire fields and values.
    :type raw_source: dict

    :param model: A dictionary containing validation rules for each field.
    :type model: dict

    :param result: A dictionary containing the validation result.
                    It should have 'status' key with a boolean value (True initially),
                   and 'errors' key with an empty list to store error messages
                   if any validation rules are violated.
    :type result: dict

    :return: The modified 'result' dictionary after checking for missing or empty values.
    :rtype: dict
    """

    for key, rules in model.items():
        if key in raw_source:
            value = raw_source[key]

            if rules.get('required', True):
                if value is None or value.strip() == "":
                    result['status'] = False
                    result['errors'].append(f"The value for '{key}' must not be None, "
                                            f"empty, or contain only whitespace")

    return result
