"""
The module contains test cases for the function validate_required
"""

import os
import unittest

import yaml

from intel.source.validate.required import validate_required


class TestValidateRequired(unittest.TestCase):
    """
    The class contains two cases to test the function.
    1) All data is present. We expect a positive result.
    2) The required callsign field is missing, we expect an error.
    """

    def test_required_fields_present(self):
        """
        The test case contains test data to verify that
        the function works correctly with the correct data entered.
        """

        raw_source = {
            "callsign": "John Doe",
            "invited by": 'WE2PY4F',
            "tags": "important information"
        }

        current_dir = os.path.dirname(os.path.abspath(__file__))
        source_yaml_path = os.path.join(current_dir, "..", "models", "source.yaml")

        with open(source_yaml_path, "r", encoding="utf-8") as file:
            model = yaml.safe_load(file)

        result = {"status": True, "errors": []}

        updated_result = validate_required(raw_source, model, result)

        self.assertTrue(updated_result["status"], "All required fields should be present")

    def test_missing_required_field(self):
        """
        The test case contains test data to verify that
        the function works correctly with missing data.
        We expect the result dictionary to be returned with an error.
        """

        raw_source = {
            "invited by": 'WE2PY4F',
            "tags": "important information"
        }

        current_dir = os.path.dirname(os.path.abspath(__file__))
        source_yaml_path = os.path.join(current_dir, "..", "models", "source.yaml")

        with open(source_yaml_path, "r", encoding="utf-8") as file:
            model = yaml.safe_load(file)

        result = {"status": True, "errors": []}

        updated_result = validate_required(raw_source, model, result)

        self.assertFalse(updated_result["status"], "The 'name' field is missing and should be detected as required")


if __name__ == '__main__':
    unittest.main()
