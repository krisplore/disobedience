"""
Module containing test cases for the 'get_time' function.

This module provides test cases to verify the behavior of the 'get_time'
function in accurately retrieving the current time.

Test cases:
- TestGetTime: Test case for retrieving the current time.
"""

import time
import unittest
from intel.source.functions import get_time


class TestGetTime(unittest.TestCase):
    """
    Test case for retrieving the current time using the 'get_time' function.

    This test case verifies that the 'get_time' function accurately retrieves
    the current time. It also checks that subsequent calls to the function
    return later timestamps.

    Methods:
        test_get_time: Test if function returns a later timestamp when called multiple times.
    """
    def test_get_time(self):
        """
        Checks if the function returns a later timestamp when called multiple times.

        Expected behavior:
            The function should accurately retrieve the current time.
            Subsequent calls to the function should return later timestamps.
        """
        time1 = get_time()
        time.sleep(1)
        time2 = get_time()

        self.assertTrue(time2 > time1)


if __name__ == '__main__':
    unittest.main()
