import unittest
from add_source_functions import extract_tags


class TestExtractTags(unittest.TestCase):
    def test_extract_tags(self):
        tags_string = 'tag1, tag2, tag3'
        expected_tags = ['tag1', 'tag2', 'tag3']
        self.assertEqual(extract_tags(tags_string), expected_tags)


if __name__ == '__main__':
    unittest.main()
