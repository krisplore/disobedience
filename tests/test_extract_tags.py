"""
Module containing test cases for the 'extract_tags' function.

This module provides test cases to verify the behavior of the 'extract_tags' function
in extracting tags from a string.

Test cases:
- TestExtractTags: Test case for extracting tags from a string.
"""

import unittest
from intel.source.functions import extract_tags


class TestExtractTags(unittest.TestCase):
    """
    Test case for extracting tags from a string using the 'extract_tags' function.

    This test case verifies that the 'extract_tags' function correctly splits a string
    by commas and removes spaces at the beginning and end of each tag. It checks that
    the function returns a list of tags without spaces.

    Methods:
        test_extract_tags: Test extracting tags from a string.
    """
    def test_extract_tags(self):
        """
        Test extracting tags from a string.

        Expected behavior:
            The function should split the string by comma and remove spaces at the beginning
            and end of each tag. It should return a list of tags without spaces.
        """
        tags_string = 'tag1 , tag2 , tag3 '
        expected_tags = ['tag1', 'tag2', 'tag3']
        self.assertEqual(extract_tags(tags_string), expected_tags)


if __name__ == '__main__':
    unittest.main()
