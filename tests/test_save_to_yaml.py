"""
Module containing test cases for the 'save_to_yaml' function.

This module provides test cases to verify the behavior of the 'save_to_yaml'
function in saving a dictionary to a YAML file.

Test cases:
- MyTestSaveToYAML: Test case for saving a dictionary to a YAML file.
"""
import os
import unittest
from intel.source.yaml_functions import save_to_yaml
import os


class MyTestSaveToYAML(unittest.TestCase):
    """
    Test case for saving a dictionary to a YAML file using the 'save_to_yaml' function.

    This test case verifies that the 'save_to_yaml' function correctly saves a dictionary
    to a YAML file. It checks that the file is created and exists.

    Methods:
        test_save_to_yaml: Test saving a dictionary to a YAML file.
    """

    def test_save_to_yaml(self):
        """
        Test saving a dictionary to a YAML file.

        It verifies that the file is created and exists.

        :return: None
        """
        source = {
            'test_key1': 'value1',
            'test_key2': 'value2',
            'test_key3': 'value3'
        }
        filename = 'test_file.yaml'

        save_to_yaml(source, filename)

        self.assertTrue(os.path.exists(filename))

        os.remove(filename)


if __name__ == '__main__':
    unittest.main()
