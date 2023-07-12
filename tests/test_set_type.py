import unittest
from intel.source.functions import set_type


class SetTypeTestCase(unittest.TestCase):
    def test_set_type(self):
        """
        The function should return 1 as code for human source.

        Expected behavior:
            The function should return the value 1.
        """
        result = set_type()
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
