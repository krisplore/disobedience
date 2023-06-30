import unittest
from src.lib.command_line_parser import parse_command_line


class MyTestParseCommandLine(unittest.TestCase):
    def test_parse_command_line(self):
        argv = ['-c', 'Johny', '-i', 'AER24MK', '-t', 'farmer, military']
        result = parse_command_line(argv)
        expected_result = [('-c', 'Johny'), ('-i', 'AER24MK'), ('-t', 'farmer, military')]
        self.assertEqual(result, expected_result, 'Parser should return lisf of tuples')  # add assertion here


if __name__ == '__main__':
    unittest.main()
