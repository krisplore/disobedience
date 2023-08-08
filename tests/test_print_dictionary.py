"""
This module contains a unit test for the 'print_dictionary' function
in the 'intel.source.functions' module.

The 'print_dictionary' function is responsible for printing the key-value pairs
of a given dictionary in a specific format.
"""

import sys
import unittest
import io
from io import StringIO

from intel.definitions import PATH_TO_SOURCE_MODEL, SOURCE_EXTENSION_YAML
from intel.source.functions import print_dictionary
from intel.source.yaml import load


class TestCasePrintDictionary(unittest.TestCase):
    """
    The 'print_dictionary' function is tested here by checking if it correctly prints the key-value pairs
    of a dictionary in the expected format.

    Test methods within this class include 'test_print_dictionary',
    which executes the test for the 'print_dictionary' function.
    """
    captured_output: StringIO

    def test_print_dictionary(self):
        """Test case for the 'print_dictionary' function.

        This method tests by capturing its output and comparing it with the expected output.

        Expected behavior:
            - The 'print_dictionary' function should correctly print the key-value pairs of the given dictionary
            in the specified format.
            - The output should be a string with each key-value pair represented in the format:
            "key: value", and each pair separated by a new line character ("\n").
        """

        test_dictionary = {
            'test key 1': 'test value',
            'test key 2': 'test value',
            'test key 3': 'test value'
        }

        self.captured_output = io.StringIO()
        sys.stdout = self.captured_output

        print_dictionary(test_dictionary, load(PATH_TO_SOURCE_MODEL + SOURCE_EXTENSION_YAML))

        output = self.captured_output.getvalue()

        expected_output = 'test key 1: test value\ntest key 2: test value\ntest key 3: test value'

        sys.stdout = sys.stdout

        self.assertEqual(output.strip(), expected_output)


if __name__ == '__main__':
    unittest.main()
