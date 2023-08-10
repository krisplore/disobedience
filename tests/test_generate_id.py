"""
Module containing test cases for the 'generate_id' function.

This module provides test cases to verify the behavior of the 'generate_id'
function in generating unique strings as IDs.

Test cases:
- TestGenerateID: Test case for generating unique IDs.
"""

import unittest

from intel.source.functions import generate_id


class TestCaseGenerateID(unittest.TestCase):
    """
    Test case for the generate_id function.

    This test case verifies the behavior of the generate_id function
    to ensure that it generates unique strings as IDs.

    Methods:
        test_unique_id: Checks if function generates unique strings as IDs.
    """

    def test_generate_id(self):
        """
        Checks if function generates unique strings as IDs.

        Expected behavior:
            The function should generate unique IDs.
        """
        source_ad = generate_id()
        source_ad2 = generate_id()
        self.assertNotEqual(source_ad, source_ad2, 'Already have this one')


if __name__ == '__main__':
    unittest.main()
