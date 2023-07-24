"""
The 'source_validator' module provides utility function for data validation and verification.

This module contains the following function:
    - validate: Check if all required fields are present in the data dictionary and have non-empty values.
"""


def validate(raw_source: dict, model) -> dict:
    """
    Check if all required fields are present in the data dictionary and have non-empty values.

    :param model: A dictionary containing validation rules for each field.
    :type model: dict

    :param raw_source: A dictionary representing the questionnaire fields and values.
    :type raw_source: dict

    :return: A dictionary with the result of the checks. It contains the 'status' key, which indicates
             whether all required fields are present and have non-empty values (True if valid, False otherwise),
             and the 'errors' key, which contains a list of error messages if any validation rules are violated.
             If no errors are found, the 'errors' list will be empty.
    :rtype: dict
    """

    result = {
        'status': True,
        'errors': []
    }

    for key, rules in model.items():
        if rules.get('required', False) and key not in raw_source:
            result['status'] = False
            result['errors'].append(f'Missing argument {key}')

        if key in raw_source:
            value = raw_source[key]

            if key != 'tags' and (value is None or not value.strip()):
                result['status'] = False
                result['errors'].append(f'{key} cannot be empty or whitespace')

            if 'min length' in rules and len(value) < rules['min length']:
                result['status'] = False
                result['errors'].append(f'The length of the {key} must be between 2 and 16 characters')
            if 'max length' in rules and len(value) > rules['max length']:
                result['status'] = False
                result['errors'].append(f'The length of the {key} must be between 2 and 16 characters')

    return result
