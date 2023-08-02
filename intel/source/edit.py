#!/usr/bin/env python3

import getopt
import sys
import yaml

from intel.definitions import PATH_TO_SOURCE_MODEL, SOURCE_EXTENSION_YAML
from intel.source.functions import extract_items_from_list, print_dictionary
from intel.source.my_yaml import read
from intel.source.validate.validator import validate


def edit():
    user_id = ''
    raw_tags = ''

    try:
        opts, args = getopt.getopt(sys.argv[1:], '', ['where.id=', 'new.tags='])
    except getopt.GetoptError as err:
        print(str(err))
        sys.exit(2)

    for opt, arg in opts:
        if opt in '--where.id':
            user_id = arg
        elif opt in '--new.tags':
            raw_tags = arg

    arguments = {
        'id': user_id,
        'tags': extract_items_from_list(raw_tags),
    }

    filename = arguments['id']

    with open(filename + SOURCE_EXTENSION_YAML, 'r', encoding='utf-8') as f:
        file: dict = yaml.safe_load(f)

    file['tags'] = arguments['tags']

    result = validate(file, read(PATH_TO_SOURCE_MODEL + SOURCE_EXTENSION_YAML))

    if not result['status']:
        print(result)
        sys.exit(2)

    else:
        with open(filename + SOURCE_EXTENSION_YAML, 'w', encoding='utf-8') as new_file:
            yaml.dump(file, new_file)
        print_dictionary(result, read(PATH_TO_SOURCE_MODEL + SOURCE_EXTENSION_YAML))
        print_dictionary(file, read(PATH_TO_SOURCE_MODEL + SOURCE_EXTENSION_YAML))


if __name__ == "__main__":
    edit()