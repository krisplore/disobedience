"""
Module containing test cases for the 'parse_options' function.

This module provides test cases to verify the behavior of the 'parse_options'
function in parsing a list of command line arguments and returning a dictionary
representing the parsed options and their corresponding arguments.

Test cases:
- MyTestParseOptions: Test case for parsing command line arguments.
"""
import unittest

from intel.source.load.options import parse_options


class TestCaseParseOptions(unittest.TestCase):
    """
    Test case for parsing command line arguments using the 'parse_options' function.

    This test case verifies that the 'parse_options' function correctly parses
    a list of command line arguments and returns the expected dictionary.

    Methods:
        test_parse_options: Test if function parses command line arguments correctly.
    """

    def test_parse_options(self):
        """
        The function parse_options should take a list of command line arguments and return a dict
        representing the parsed options and their corresponding arguments.

        The test case provides a sample list of command line arguments.

        Expected behavior:
            The function should correctly parse the command line arguments and return the expected dict.
            The length of the return list of the function is not less than the required options.
        """

        argv = ['-c', 'Johny', '-i', 'AER24MK', '-t', 'farmer, military']
        result = parse_options(argv)
        expected_result = {'callsign': 'Johny', 'invited_by': ['AER24MK'], 'tags': ['farmer', 'military']}
        self.assertEqual(result, expected_result, 'Parser should return dict')
        #  self.assertTrue(len(result) >= len(REQUIRED_OPTIONS_FULL), 'Missing required arguments')


if __name__ == '__main__':
    unittest.main()
