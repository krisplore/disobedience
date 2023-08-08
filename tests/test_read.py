"""
Module: test_read_function.py

This module contains unit test for the 'read' function in the 'intel.source.yaml' module.
"""
import os
import unittest

from intel.source.yaml import read


class TestRead(unittest.TestCase):
    """
    Test suite for the 'read' function.

    This class contains unit test for the 'read' function, which reads data from a YAML file
    and returns the parsed content as a Python dictionary.
    """

    def test_read(self):
        """
        Test reading data from a valid YAML file.

        This test case checks whether the 'read' function can correctly read data from a valid YAML file
        and parse it into a Python dictionary. It compares the result with the expected content of the file.
        """

        filename = os.path.join(os.path.dirname(__file__), 'test_files', 'test.yaml')
        expected_data = {
            'callsign': 'Jack',
            'invited by': 'WEQ24UA',
            'tags': ['tag1', 'tag2', 'tag3', 'tag4']
        }

        result = load(filename)

        self.assertEqual(result, expected_data, "Parsed content doesn't match expected data.")


if __name__ == '__main__':
    unittest.main()
