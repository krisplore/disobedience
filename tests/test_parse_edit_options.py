"""
Module to test the function parse_edit_options. Contains a test case TestParseEditOptions.
"""
import unittest
from intel.source.edit_parser import parse_edit_options


class TestParseEditOptions(unittest.TestCase):
    """
    Test case for parse_edit_options function.

    Methods:
        test_parse_edit_options: Test parsing edit options from command line.
    """
    def test_parse_edit_options(self):
        """
        Test parsing edit options from command line.

        Expected behavior:
            The function should correctly parse the command line options and values and
            return a dictionary containing the parsed data.
        """

        argv = ['--where.id', 'test_id', '--new.callsign', 'JohnD']
        result = parse_edit_options(argv)
        expected_result = {
            'id': 'test_id',
            'callsign': 'JohnD'
        }
        self.assertEqual(result, expected_result, 'Parser should return dict')


if __name__ == '__main__':
    unittest.main()
