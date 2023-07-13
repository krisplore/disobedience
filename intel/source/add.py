"""
Responsible for managing the process of adding a new source.
"""

import sys              #
import gettext          # translate the strings
from intel.source.input_data import parse_options, parse_filename
from intel.source.functions import create_source_stub, \
    print_source_information, validator
from intel.source.yaml_functions import save_to_yaml
from intel.definitions import PATH_BASE, SOURCE_EXTENSION_YAML, NAME_PROJECT
from intel.source.input_data import parse_input_method
from intel.source.yaml_functions import read_from_yaml

_: None = None
PATH_TO_LOCALES: str = PATH_BASE + '/locales'
PATH_TO_STORAGE: str = PATH_BASE + '/data/source/'


def add():
    """
    This function handles the process of adding a new data source.
    It prompts the user for required information, generates relevant data,
    and saves it to a file.
    """

    global _
    language = gettext.translation(NAME_PROJECT, localedir=PATH_TO_LOCALES)
    language.install()
    _ = language.gettext

    print(_("Language"))

    source = create_source_stub()

    input_method = parse_input_method()

    match input_method:
        case 'file':
            data_input = read_from_yaml(parse_filename(sys.argv[4:]))
        case 'options':
            data_input = parse_options(sys.argv[4:])
        case _:
            print(_('Method does not exist'))
            sys.exit(2)

    status_info = validator(data_input)

    if not status_info['status']:
        print_source_information(_(status_info['errors']))
        sys.exit(2)
    else:
        print_source_information(status_info)
        source.update(data_input)

        filename: str = PATH_TO_STORAGE + id_value + SOURCE_EXTENSION_YAML
        save_to_yaml(source, filename)
        print_source_information(source)
