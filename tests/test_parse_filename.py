"""
Module containing test case for the 'parse_filename' function.

This module provides test case to verify the behavior of the 'parse_filename'
function in parsing a list of command line arguments and returning a string
representing the name of file for input data.

Test case:
- TestCaseParseFilename: Test case for parsing command line arguments.
"""

import unittest

from intel.source.load.input_file import parse_filename


class TestCaseParseFilename(unittest.TestCase):
    """
    Test case for parsing command line arguments using the 'parse_filename' function.

    This test case verifies that the 'parse_filename' function correctly parses
    a list of command line arguments and returns the expected string - filename.

    Methods:
    test_parse_filename: Test if function parses command line arguments correctly.
    """
    def test_parse_filename(self):
        """
        The function parse_filename should take a list of command line arguments and return a string
        representing the name of file.

        The test case provides a sample list of command line arguments.

        Expected behavior:
            The function should correctly parse the command line arguments and return the expected string.
            The string has to be not empty.
        """
        argv = ['-f', 'test-filename']
        result = parse_filename(argv)
        expected_result = 'test-filename'
        self.assertIsInstance(result, str, 'Parser should return a string')
        self.assertEqual(expected_result, result, 'Parser should return an expected result')
        self.assertTrue(len(result), 'Parser should return not an empty string')


if __name__ == '__main__':
    unittest.main()
