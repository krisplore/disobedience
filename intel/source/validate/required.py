"""
The 'required' module provides utility function for data validation.

This module contains the following function:
    - validate_required: Check if all required fields are present in the data dictionary.
"""
import logging

py_logger7 = logging.getLogger(__name__)
py_logger7.setLevel(logging.INFO)

py_handler = logging.FileHandler(f"logs/{__name__}.log", mode='w')
py_formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

py_handler.setFormatter(py_formatter)
py_logger7.addHandler(py_handler)


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
    py_logger7.info("validate_required function was called")

    for key, rules in model.items():
        if rules.get('required', False) and key not in raw_source:
            py_logger7.warning("Missing argument: %s", key)
            result['status'] = False
            result['errors'].append(f'Missing argument {key}')

        if key in raw_source:
            value = raw_source[key]

            if rules.get('required', True) and rules.get('type') == 'string':
                if value is None or value.strip() == "":
                    py_logger7.warning("Invalid value for '%s'. It must not be None, empty, "
                                       "or contain only whitespace.", key)
                    result['status'] = False
                    result['errors'].append(f"The value for '{key}' must not be None, "
                                            f"empty, or contain only whitespace")

    return result
