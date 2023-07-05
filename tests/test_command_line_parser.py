import unittest
from src.lib.input.command_line_parser import *


class MyTestParseCommandLine(unittest.TestCase):
    def test_parse_command_line(self):
        """
        The function parse_command_line should take a list of command line arguments and return a dict
        representing the parsed options and their corresponding arguments.

        The test case provides a sample list of command line arguments.

        Expected behavior:
            The function should correctly parse the command line arguments and return the expected dict.
            The length of the return list of the function is not less than the required options.
        """
        argv = ['-c', 'Johny', '-i', 'AER24MK', '-t', 'farmer, military']
        result = parse_command_line(argv)
        expected_result = {'-c': 'Johny', '-i': 'AER24MK', '-t': 'farmer, military'}
        self.assertEqual(result, expected_result, 'Parser should return dict')
        #  self.assertTrue(len(result) >= len(REQUIRED_OPTIONS_FULL), 'Missing required arguments')


if __name__ == '__main__':
    unittest.main()
