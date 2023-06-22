import unittest
import uuid


def generate_id():
    return str(uuid.uuid4())


class TestGenerateID(unittest.TestCase):
    def test_unique_id(self):
        ids = []  # сравнить 2
        amount_of_ids = 100

        for _ in range(amount_of_ids):
            source_ad = generate_id()
            self.assertIsNot(source_ad, ids, 'Already have this one')
            ids.append(source_ad)

        self.assertEqual(len(ids), amount_of_ids, 'The amount of IDs is not as expected')


if __name__ == '__main__':
    unittest.main()
