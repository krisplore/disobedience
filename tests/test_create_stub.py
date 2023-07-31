"""
The module contains a test case for the create_stub function
"""
import os
import unittest
from unittest.mock import patch
import yaml
from intel.source.functions import create_stub


class TestCreateStub(unittest.TestCase):
    """
    The class contains a test case for the function.
    The function must return the created stub - a dictionary.
    """
    def test_return_type(self):
        """
        The test case is built on the use of a patch in order to open the model in the test
        and get as close as possible to natural conditions without changing the function.
        The function must return a dictionary
        """
        current_dir = os.path.dirname(os.path.abspath(__file__))
        source_yaml_path = os.path.join(current_dir, "..", "models", "source.yaml")

        with open(source_yaml_path, "r", encoding="utf-8") as file:
            model = yaml.safe_load(file)

        with patch("intel.source.functions.read", return_value=model):
            result = create_stub()

        self.assertIsInstance(result, dict, "The function must return a dictionary")


if __name__ == '__main__':
    unittest.main()
