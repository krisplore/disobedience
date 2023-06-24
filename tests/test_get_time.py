import time
import unittest
import datetime
from add_source_functions import get_time


class TestGetTime(unittest.TestCase):
    def test_get_time(self):
        time1 = get_time()
        time.sleep(1)
        time2 = get_time()

        self.assertTrue(time2 > time1)


if __name__ == '__main__':
    unittest.main()
