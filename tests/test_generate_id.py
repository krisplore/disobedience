import unittest
import uuid


def generate_id():
    return str(uuid.uuid4())


class TestGenerateID(unittest.TestCase):
    def test_unique_id(self):
        source_ad = generate_id()
        source_ad2 = generate_id()
        self.assertNotEqual(source_ad, source_ad2, 'Already have this one')


if __name__ == '__main__':
    unittest.main()