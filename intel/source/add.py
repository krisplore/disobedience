"""
Responsible for managing the process of adding a new source.
"""

import sys              #
import gettext          # translate the strings
from intel.source.input_data import parse_options, parse_filename
from intel.source.functions import extract_tags, create_source_stub, \
    print_source_information
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

    source, id_value = create_source_stub()

    # source: dict[str | Any, int | str | object | float | Any] = {
    #     '_source_schema_version': SOURCE_SCHEMA_VERSION,
    #     'callsign':     callsign,
    #     'tags':         raw_tags,
    #     'invited_by':   invited_by,
    #     'id':           id_value,
    #     'type':         set_type(),
    #     'reliability':  4.98,
    #     'note':         'some new note',
    #     'created':      creation_time,
    #     'modified':     modification_time,
    #     'invite':       generate_invite(),
    #     'stats': {
    #         'total facts':      0,
    #         'confirmed facts':  0,
    #         'refuted facts':    0
    #     }
    # }

    input_method = parse_input(sys.argv[3:])
    print(input_method)

    for key, value in opts.items():
        for map_key, map_value in option_map.items():
            if key in map_value:
                source[map_key] = value
                break
    # print(type(opts), opts)



    raw_tags = source['tags']
    source['tags'] = extract_tags(raw_tags)

    filename: str = PATH_TO_STORAGE + id_value + EXTENSION_YAML
    save_to_yaml(source, filename)
