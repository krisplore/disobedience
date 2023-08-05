"""
The 'source_validator' module provides utility function for data validation and verification.

This module contains the following function:
    - validate: Check if all required fields are present in the data dictionary and have non-empty values.
"""
import logging

from intel.source.validate.length import validate_length
from intel.source.validate.required import validate_required

py_logger6 = logging.getLogger(__name__)
py_logger6.setLevel(logging.INFO)

py_handler = logging.FileHandler(f"logs/{__name__}.log", mode='w')
py_formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

py_handler.setFormatter(py_formatter)
py_logger6.addHandler(py_handler)


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
    py_logger6.info("validate function was called")

    result = {
        'status': True,
        'errors': []
    }

    result = validate_required(raw_source, model, result)
    py_logger6.info("Result after validate_required received")
    result = validate_length(raw_source, model, result)
    py_logger6.info("Result after validate_length received")

    return result
