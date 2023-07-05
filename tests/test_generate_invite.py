import unittest
from src.lib.process.functions import *


class MyTestGenerateInvite(unittest.TestCase):
    def test_generate_invite(self):
        """
        Checks if the function generate unique invites

        Expected behavior:
            The function should generate unique invites.
            The generated invites should not contain whitespace characters.
            The length of each invite should be equal to INVITE_LENGTH.
        """
        invite = generate_invite()
        for token in invite:
            self.assertFalse(token.isspace(), 'Invite should not be a whitespace character')
            self.assertEqual(INVITE_LENGTH, len(token), f'The length of the invite must be = {INVITE_LENGTH}')
        self.assertEqual(len(invite), len(set(invite)), 'Invites are not unique')


if __name__ == '__main__':
    unittest.main()
