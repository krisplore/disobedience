"""
The model provides a test case for the function generate_options.
"""
import unittest
from pathlib import Path

import yaml

from intel.source.generator import generate_options


class MyTestCase(unittest.TestCase):
    """
    The test case checks that the function returns the expected result -
    a list of options for the command line.
    """
    def test_something(self):
        """
        The function is given a test model, according to which it will make a list of options for the command line.
        """
        base = str(Path(__file__).parent.parent)
        filename = base + '/tests/test_files/test_model.yaml'
        with open(filename, 'r', encoding='utf-8') as file:
            model: dict = yaml.safe_load(file)
        result = generate_options(model)
        expected_result = ['where.id=', 'new.callsign=', 'new.invited-by=', 'new.tags=', 'new.invite=',
                           'new.type=', 'new.reliability=', 'new.note=']
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
