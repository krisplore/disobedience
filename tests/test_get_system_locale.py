"""
This module is responsible for testing the get_system_locale
function by adding a patch to the program
"""

import unittest
from unittest.mock import patch
from intel.source.functions import get_system_locale


class TestGetSystemLocale(unittest.TestCase):
    """
    The test class contains two cases:
    1) locale not provided, automatic substitution of en_US is expected
    2) specifies the system locale
    """

    def test_get_system_locale_with_no_locale(self):
        """
        Test for get_system_locale() when the system locale is not defined.
        Expected behavior: get_system_locale() should return 'en_US'.
        """

        with patch('babel.default_locale', return_value=None):
            result = get_system_locale()
            self.assertEqual(result, 'en_US', 'get_system_locale() should return "en_US" '
                                              'when the system locale is not defined')

    @patch('babel.default_locale', return_value='en_US')
    def test_get_system_locale_with_locale(self, mock_default_locale):
        """
        Test for get_system_locale() when the system locale is defined.
        Expected behavior: get_system_locale() should return the system locale, which is 'en_US'.
        """
        result = get_system_locale()
        self.assertEqual(result, mock_default_locale.return_value,
                         'get_system_locale() should return the system locale')


if __name__ == '__main__':
    unittest.main()
