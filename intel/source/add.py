"""
Responsible for managing the process of adding a new source.
"""

import sys

from intel.definitions import SOURCE_EXTENSION_YAML, PATH_TO_SOURCE_MODEL
from intel.source.functions import create_stub, print_dictionary
from intel.source.load.file import parse_filename
from intel.source.load.input_method import parse_method_input
from intel.source.load.input_options import parse_options
from intel.source.validate.validator import validate
from intel.source.yaml_functions import read_from_yaml
from intel.source.yaml_functions import save_to_yaml
from intel.translation import start_translating

_ = start_translating()


def add():
    """
    This function handles the process of adding a new data source.
    It prompts the user for required information, generates relevant data,
    and saves it to a file.
    """

    print(_("Language"))

    source = create_stub()

    method_input = parse_method_input()

    match method_input:
        case 'file':
            raw_source = read_from_yaml(parse_filename(sys.argv[4:]))
        case 'opt':
            raw_source = parse_options(sys.argv[4:])
        case _:
            print(_('Method does not exist'))
            sys.exit(2)

    success = validate(raw_source, read_from_yaml(PATH_TO_SOURCE_MODEL + SOURCE_EXTENSION_YAML))

    if not success['status']:
        print_dictionary(success)
        sys.exit(2)
    else:
        print_dictionary(success)
        source.update(raw_source)

        save_to_yaml(source, source['id'])
        print_dictionary(source)
