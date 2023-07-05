import unittest
from src.lib.process.functions import generate_id


class TestGenerateID(unittest.TestCase):
    def test_unique_id(self):
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
