"""
The model provides a test case for the function generate_options.
"""

import unittest
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
        with open('tests/test_files/test_model.yaml', 'r', encoding='utf-8') as file:
            model: dict = yaml.safe_load(file)
        result = generate_options(model)
        expected_result = ['where.id=', 'new.callsign=', 'new.invited-by=', 'new.tags=', 'new.invite=',
                           'new.type=', 'new.reliability=', 'new.note=']
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
