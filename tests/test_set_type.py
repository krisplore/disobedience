"""
Module containing test cases for the 'set_type' function.

This module provides test cases to verify the behavior of the 'set_type' function
in setting the type of source.

Test cases:
- SetTypeTestCase: Test case for setting the type of source.
"""

import unittest
from intel.source.functions import set_type


class SetTypeTestCase(unittest.TestCase):
    """
    Test case for setting the type of source using the 'set_type' function.

    This test case verifies that the 'set_type' function correctly sets the type
    of source and returns the expected value.

    Methods:
        test_set_type: Test setting the type of source.
    """
    def test_set_type(self):
        """
        Test setting the type of source.

        Expected behavior:
            The function should return the value 1.
        """
        result = set_type()
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
