"""
Module containing test cases for the 'generate_invite' function.

This module provides test cases to verify the behavior of the 'generate_invite'
function in generating unique invites.

Test cases:
- MyTestGenerateInvite: Test case for generating unique invites.
"""

import unittest

from intel.definitions import PATH_TO_SOURCE_MODEL, SOURCE_EXTENSION_YAML
from intel.source.functions import generate_invite
from intel.source.yaml import load


class TestCaseGenerateInvite(unittest.TestCase):
    """
    Test case for generating unique invites using the 'generate_invite' function.

    This test case verifies that the 'generate_invite' function generates unique
    invites. It also checks that the generated invites do not contain whitespace
    characters and have a length equal to INVITE_LENGTH.

    Methods:
        test_generate_invite: Test if function generates unique invites.
    """
    def test_generate_invite(self):
        """
        Checks if the function generate unique invites.

        Expected behavior:
            The function should generate unique invites.
            The generated invites should not contain whitespace characters.
            The length of each invite should be equal to INVITE_LENGTH.
        """
        model = read(PATH_TO_SOURCE_MODEL + SOURCE_EXTENSION_YAML)
        invite = generate_invite(model)
        invite_length = model['invite']['item']['length']
        for token in invite:
            self.assertFalse(token.isspace(), 'Invite should not be a whitespace character')
            self.assertEqual(invite_length, len(token), f'The length of the invite must be = {invite_length}')
        self.assertEqual(len(invite), len(set(invite)), 'Invites are not unique')


if __name__ == '__main__':
    unittest.main()
