import time
import unittest
from src.lib.functions import get_time


class TestGetTime(unittest.TestCase):
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
