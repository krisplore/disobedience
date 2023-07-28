"""
The 'source_validator' module provides utility function for data validation and verification.

This module contains the following function:
    - validate: Check if all required fields are present in the data dictionary and have non-empty values.
"""
from intel.source.validate.empty_string import validate_emptiness
from intel.source.validate.length import validate_length
from intel.source.validate.required import validate_required


def validate(raw_source: dict, model: dict) -> dict:
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

    result = validate_required(raw_source, model, result)
    result = validate_emptiness(raw_source, model, result)
    result = validate_length(raw_source, model, result)

    return result
