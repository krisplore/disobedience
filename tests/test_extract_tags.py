"""
Module containing test cases for the 'test_items_from_list' function.

This module provides test cases to verify the behavior of the 'test_items_from_list' function
in extracting tags from a string.

Test cases:
- TestCaseExtractItemsFromList: Test case for extracting tags from a string.
"""

import unittest
import yaml
from intel.source.functions import extract_items_from_list


class TestCaseExtractItemsFromList(unittest.TestCase):
    """
    Test case for extracting tags from a string using the 'test_items_from_list' function.

    This test case verifies that the 'test_items_from_list' function correctly splits a string
    by commas and removes spaces at the beginning and end of each tag. It checks that
    the function returns a dict of list of tags without spaces.

    Methods:
        test_items_from_list: Test extracting tags from a string.
    """
    def test_items_from_list(self):
        """
        Test extracting tags from a string.

        Expected behavior:
            The function should split the string by comma and remove spaces at the beginning
            and end of each tag. It should return a dict with list of tags without spaces.
        """
        with open('models/source.yaml', 'r', encoding='utf-8') as file:
            model: dict = yaml.safe_load(file)

        new_values = {'tags': '  tag1 , tag2 , tag3 '}
        expected_values = {'tags': ['tag1', 'tag2', 'tag3']}
        extract_items_from_list(new_values, model)
        self.assertEqual(new_values, expected_values)


if __name__ == '__main__':
    unittest.main()
