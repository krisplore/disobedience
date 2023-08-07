"""
The module provides a test case to test the function replace_hyphen_with_underscore.
"""
import unittest

from intel.source.functions import synch_name


class TestCaseSwitchFunction(unittest.TestCase):
    """
    The test case provides one case for the function to work correctly.
    Expected result: The function will return a string with dashes replaced with underscores.
    """

    def test_replace_hyphen_with_underscore(self):
        """
        The test gives a line for the switch. The function should return the expected result.
        """

        test_data = 'invited-by-John'
        expected_result = 'invited_by_John'
        result = synch_name(test_data)
        self.assertEqual(result, expected_result, 'The function should return the expected result.')


if __name__ == '__main__':
    unittest.main()
