#!/usr/bin/env python3

import getopt
import sys

from intel.definitions import PATH_TO_SOURCE_MODEL, SOURCE_EXTENSION_YAML, PATH_TO_STORAGE
from intel.source.edit_parser import parse_edit_options
from intel.source.functions import print_dictionary
from intel.source.my_yaml import read, write
from intel.source.validate.validator import validate


def edit():
    user_id = ''
    raw_tags = ''

    try:
        opts, args = getopt.getopt(sys.argv[1:], '', ['where.id=', 'new.tags='])
    except getopt.GetoptError as err:
        print(str(err))
        sys.exit(2)

    arguments = parse_edit_options(sys.argv[3:])

    filename = arguments['id']

    source = read(PATH_TO_STORAGE + filename + SOURCE_EXTENSION_YAML)

    source.update(arguments)

    model = read(PATH_TO_SOURCE_MODEL + SOURCE_EXTENSION_YAML)

    result = validate(source, model)

    if not result['status']:
        print(result)
        sys.exit(2)

    else:
        write(source, filename)

        print_dictionary(result, model)
        print_dictionary(source, model)
