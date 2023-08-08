"""
The 'length' module provides utility functions for data validation.

This module contains the following function:
    - validate_length: Check if the length of specified fields in the data dictionary
    meets the validation rules.

Note: This module is designed for use with Python 3.x.
"""

from intel.log import setup_logger

logger = setup_logger()


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
    logger.info("validate_length function was called")

    for field, properties in model.items():
        if 'length' in properties:
            if field in raw_source:
                value = raw_source[field]
                if not isinstance(value, (str, list)):
                    if ('length' in properties and 'min' in properties['length']
                            and len(value) < properties['length']['min']):
                        result['status'] = False
                        result['errors'].append(f'The length of the {field} must be between '
                                                f'{properties["length"]["min"]} and '
                                                f'{properties["length"]["max"]} characters')

                        logger.warning("Invalid length for '%s'. Length must be between %s and %s "
                                       "characters.", field, properties["length"]["min"],
                                       properties["length"]["max"])

                    if ('length' in properties and 'max' in properties['length']
                            and len(value) > properties['length']['max']):
                        result['status'] = False
                        result['errors'].append(f'The length of the {field} must be between '
                                                f'{properties["length"]["min"]} and '
                                                f'{properties["length"]["max"]} characters')

                        logger.warning("Invalid length for '%s'. Length must be between %s and %s "
                                       "characters.", field, properties["length"]["min"],
                                       properties["length"]["max"])

    return result
