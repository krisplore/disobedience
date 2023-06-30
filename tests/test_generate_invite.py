import unittest
from src.lib.functions import *


class MyTestGenerateInvite(unittest.TestCase):
    def test_generate_invite(self):
        invite = generate_invite()
        for token in invite:
            self.assertFalse(token.isspace(), 'Invite should not be a whitespace character')
            self.assertEqual(INVITE_LENGTH, len(token), f'The length of the invite must be = {INVITE_LENGTH}')
        self.assertEqual(len(invite), len(set(invite)), 'Invites are not unique')


if __name__ == '__main__':
    unittest.main()
