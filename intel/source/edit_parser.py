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

    user_id = ''
    raw_tags = ''

    try:
        opts, args = getopt.getopt(argv, '', ['where.id=', 'new.tags='])
    except getopt.GetoptError as err:
        print(str(err))
        sys.exit(2)

    for opt, arg in opts:
        if opt == '--where.id':
            user_id = arg
        elif opt == '--new.tags':
            raw_tags = arg

    parse_arguments = {
        'id': user_id,
        'tags': extract_items_from_list(raw_tags),
    }

    return parse_arguments
