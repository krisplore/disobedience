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

    for field, properties in model.items():
        if properties.get('type') == 'list string separator comma':
            value = raw_source.get(field)

            if value is not None:
                if not isinstance(value, (str, list)):
                    result['status'] = False
                    result['errors'].append(f"Invalid value for field '%s'. Expected a string or a list.", field)

                    py_logger8.warning(f"Invalid value for field '{field}'. Expected a string or a list.")

                elif isinstance(value, list):
                    min_length = properties.get('length', {}).get('min')
                    if min_length is not None and len(value) < min_length:
                        result['status'] = False
                        result['errors'].append(f"Field '{field}' must have at least {min_length} items.")

                        py_logger8.warning(f"Field '%s' must have at least {min_length} items.", field)

                    item_length = properties.get('item', {}).get('length')
                    py_logger8.info(f"Item length for field '%s' is %s", field, item_length)
                    if item_length is not None:
                        for item in value:
                            if not isinstance(item, str):
                                result['status'] = False
                                result['errors'].append(f"Invalid value for field '{field}'."
                                                        f"Expected a string or a list.")

                                py_logger8.warning(f"Invalid value for field '%s'. Expected a string or a list.", field)

                            elif len(item) != item_length:
                                result['status'] = False
                                result['errors'].append(f"Each item in field '{field}' must have length {item_length}.")

                                py_logger8.warning(f"Each item in field '%s' must have length {item_length}.", field)

        if 'length' in properties:
            if field in raw_source:
                value = raw_source[field]
                if not isinstance(value, (str, list)):
                    if 'length' in properties and 'min' in properties['length'] and len(value) < properties['length']['min']:
                        result['status'] = False
                        result['errors'].append(f'The length of the {field} must be between '
                                                f'{properties["length"]["min"]} and '
                                                f'{properties["length"]["max"]} characters')

                        py_logger8.warning("Invalid length for '%s'. Length must be between %s and %s "
                                           "characters.", field, properties["length"]["min"], properties["length"]["max"])


                    if 'length' in properties and 'max' in properties['length'] and len(value) > properties['length']['max']:
                        result['status'] = False
                        result['errors'].append(f'The length of the {field} must be between '
                                                f'{properties["length"]["min"]} and '
                                                f'{properties["length"]["max"]} characters')

                        py_logger8.warning("Invalid length for '%s'. Length must be between %s and %s "
                                           "characters.", field, properties["length"]["min"],
                                           properties["length"]["max"])

    return result
