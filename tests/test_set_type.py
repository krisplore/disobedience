import unittest
from dict_source import set_type


class SetTypeTestCase(unittest.TestCase):
    def test_set_type(self):
        result = set_type()
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
