"""
The 'length' module provides utility functions for data validation.

This module contains the following function:
    - validate_length: Check if the length of specified fields in the data dictionary
    meets the validation rules.

Note: This module is designed for use with Python 3.x.
"""
import logging

py_logger8 = logging.getLogger(__name__)
py_logger8.setLevel(logging.INFO)

py_handler = logging.FileHandler(f"logs/{__name__}.log", mode='w')
py_formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

py_handler.setFormatter(py_formatter)
py_logger8.addHandler(py_handler)


def validate_length(raw_source: dict, model: dict, result: dict):
    """
    Check if the length of specified fields in the data dictionary meets the validation rules.

    :param raw_source: A dictionary representing the questionnaire fields and values.
    :type raw_source: dict

    :param model: A dictionary containing validation rules for each field.
    :type model: dict

    :param result: A dictionary containing the validation result.
                   The function will update the 'status' key to False and
                   add error messages to 'errors' list if any validation rules are violated.
    :type result: dict

    :return: The modified 'result' dictionary after checking the length of specified fields.
    :rtype: dict
    """
    py_logger8.info("validate_length function was called")

    for key, rules in model.items():
        if 'length' in rules:
            if key in raw_source:
                value = raw_source[key]
                if not isinstance(value, (str, list)):
                    if 'length' in rules and 'min' in rules['length'] and len(value) < rules['length']['min']:
                        py_logger8.warning("Invalid length for '%s'. Length must be between %s and %s "
                                           "characters.", key, rules["length"]["min"], rules["length"]["max"])
                        result['status'] = False
                        result['errors'].append(f'The length of the {key} must be between '
                                                f'{rules["length"]["min"]} and '
                                                f'{rules["length"]["max"]} characters')

                    if 'length' in rules and 'max' in rules['length'] and len(value) > rules['length']['max']:
                        py_logger8.warning("Invalid length for '%s'. Length must be between %s and %s "
                                           "characters.", key, rules["length"]["min"], rules["length"]["max"])
                        result['status'] = False
                        result['errors'].append(f'The length of the {key} must be between '
                                                f'{rules["length"]["min"]} and '
                                                f'{rules["length"]["max"]} characters')

    return result
