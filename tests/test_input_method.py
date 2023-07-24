"""
Module containing test case for the 'parse_method_input' function.

This module provides test case to verify the behavior of the 'parse_method_input'
function in parsing a list of command line arguments and returning a string
representing the parsed method of input data.

Test case:
- TestCaseParseMethodInput: Test case for parsing command line arguments.
"""

import unittest
from unittest.mock import patch

from intel.source.input_method import parse_method_input


class TestCaseParseMethodInput(unittest.TestCase):
    """
    Test case for parsing command line arguments using the 'parse_method_input' function.

    This test case verifies that the parse_method_input' function correctly parses
    a list of command line arguments and returns the expected string - name of method.
    """

    @patch('sys.argv', ['script_name.py', 'arg1', 'arg2', 'input_method'])
    def test_parse_method_input(self):
        """
        The function parse_input_method should take a list of command line arguments and return a string
        representing the name of input.

        The test case provides a sample list of command line arguments.

        Expected behavior:
            The function should correctly parse the command line arguments and return the expected string.
            The string has to be not empty.
        """

        result = parse_method_input()
        expected_result = 'input_method'
        self.assertIsInstance(result, str, 'Parser should return a string.')
        self.assertTrue(result, 'Parser should return not an empty string. String is empty.')
        self.assertEqual(expected_result, result, 'Parser should return an expected result.')


if __name__ == '__main__':
    unittest.main()
