"""
Module containing test cases for the 'convert_date' function.

This module provides test cases to verify the behavior of the 'convert_date'
function in accurately format date values in the desired format.

Test case:
- TestConvertDate: Test case for conversion of a timestamp to a formatted date.
"""

import unittest

from intel.source.functions import convert_date


class TestConvertDate(unittest.TestCase):
    """
    This test case verifies that the 'convert_date' function accurately format date values in
    the desired format. It also checks that an error has occurred.
    """

    def test_convert_date(self):
        """
        Test Case 1: Tests the conversion of a valid timestamp to a formatted date and time for the "ru_RU" locale.

        Test Case 2: Tests the handling of an invalid value for the "ru_RU" locale.
        """

        value1 = 1679192312
        user_locale1 = 'ru_RU'
        expected_result1 = '19.03.2023, 09:18'
        self.assertEqual(convert_date(value1, user_locale1), expected_result1)

        value3 = 'InvalidValue'
        user_locale3 = 'ru_RU'
        expected_result3 = 'InvalidValue'
        self.assertEqual(convert_date(value3, user_locale3), expected_result3)


if __name__ == '__main__':
    unittest.main()
