"""
The 'required' module provides utility function for data validation.

This module contains the following function:
    - validate_required: Check if all required fields are present in the data dictionary.
"""

from intel.log import setup

logger = setup()


def validate_required(raw_source: dict, model: dict, result: dict):
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
    logger.info("validate_required function was called")

    for field, properties in model.items():
        if properties.get('required', False) and field not in raw_source:
            logger.warning("Missing argument: %s", field)
            result['status'] = False
            result['errors'].append(f'Missing argument {field}')

        if field in raw_source:
            value = raw_source[field]

            if properties.get('required', True) and properties.get('type') == 'string':
                if value is None or value.strip() == "":
                    logger.warning("Invalid value for '%s'. It must not be None, empty, "
                                   "or contain only whitespace.", field)
                    result['status'] = False
                    result['errors'].append(f"The value for '{field}' must not be None, "
                                            f"empty, or contain only whitespace")

    return result
