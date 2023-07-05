import unittest
from src.lib.process.functions import extract_tags


class TestExtractTags(unittest.TestCase):
    def test_extract_tags(self):
        """
        Check if function splits a string by comma and removes spaces at the beginning and end of each tag.

        Expected behavior:
            Should return a list of tags without spaces.
        """
        tags_string = 'tag1 , tag2 , tag3 '
        expected_tags = ['tag1', 'tag2', 'tag3']
        self.assertEqual(extract_tags(tags_string), expected_tags)


if __name__ == '__main__':
    unittest.main()
