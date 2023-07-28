"""
This module provides a test case for function for retrieving the entity
and action arguments from the command line.
"""
import unittest
from unittest.mock import patch

from intel.getopt_router import getopt_entity_action


class TestGetoptEntityAction(unittest.TestCase):
    """
    This test verifies the behavior of the function by using the 'patch' decorator
    to temporarily replace the 'sys.argv' value and check if the function correctly extracts the entity and action
    from the command line arguments.
    """

    @patch('sys.argv', ['script_name.py', 'entity_name', 'action_name'])
    def test_getopt_entity_action(self):
        """
        This test function tests the 'getopt_entity_action' function by simulating command line arguments using 'patch'
        and comparing the returned result with the expected result. The function should correctly return the entity and
        action arguments as a list.
        """

        result = getopt_entity_action()
        expected_result = ['entity_name', 'action_name']

        self.assertEqual(result, expected_result, 'Function should return the correct entity and action arguments')


if __name__ == '__main__':
    unittest.main()
