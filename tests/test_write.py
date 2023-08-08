"""
Module containing test cases for the 'save_to_yaml' function.

This module provides test cases to verify the behavior of the 'save_to_yaml'
function in saving a dictionary to a YAML file.

Test cases:
- MyTestSaveToYAML: Test case for saving a dictionary to a YAML file.
"""

import os
import unittest

from intel.definitions import SOURCE_EXTENSION_YAML
from intel.source.yaml import write, PATH_TO_STORAGE


class TestCaseSaveToYAML(unittest.TestCase):
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
        filename = 'test_file'

        save(source, filename)

        self.assertTrue(os.path.exists(PATH_TO_STORAGE + filename + SOURCE_EXTENSION_YAML))

        os.remove(PATH_TO_STORAGE + filename + SOURCE_EXTENSION_YAML)


if __name__ == '__main__':
    unittest.main()
