"""
The module is responsible for the function that retrieves the values for the options to edit the file.
"""

import getopt
import sys

from intel.source.functions import extract_items_from_list


def parse_edit_options(argv):
    """
    The function parses the options and values of the command line, to obtain the option
    where. - source file qualifier and new. - data to change.

    :param argv: command line value
    :return: a dictionary from command line values
    :rtype: dict
    """

    options = ['where.id=', 'new.tags=', 'new.note=']

    try:
        opts = getopt.getopt(argv, '', options)[0]
    except getopt.GetoptError as err:
        print(str(err))
        sys.exit(2)

    new_values = {}
    for opt, arg in opts:
        if '--where' in opt:
            key = opt[8:]
            new_values[key] = arg
        elif '--new' in opt:
            key = opt[6:]
            new_values[key] = arg

    if new_values == 'tags':
        new_values['tags'] = extract_items_from_list(new_values['tags'])

    return new_values
