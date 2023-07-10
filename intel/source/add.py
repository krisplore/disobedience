import sys              #
import gettext          # translate the strings
from gettext import NullTranslations, GNUTranslations
from typing import Dict, Tuple, Any, List

from intel.source.getopt_input import parse_input_options
from intel.source.functions import get_time, extract_tags, generate_id, generate_invite, set_type
from intel.source.save_to_yaml import save_to_yaml
from intel.definitions import PATH_BASE, SOURCE_SCHEMA_VERSION

_: None = None
EXTENSION: str = '.yaml'
PATH_TO_LOCALES: str = PATH_BASE + '/locales'
PATH_TO_STORAGE: str = PATH_BASE + '/data/source/'
NAME_PROJECT: str = 'disobedience'
_SOURCE_SCHEMA_VERSION: int = 1


def add():
    global _
    language: NullTranslations | GNUTranslations = gettext.translation(NAME_PROJECT, localedir=PATH_TO_LOCALES)
    language.install()
    _ = language.gettext

    print(_("Language"))

    option_map: dict[str, tuple[str, str]] = {
        'callsign': ('-c', '--callsign'),
        'tags': ('-t', '--tags'),
        'invited_by': ('-i', '--invited_by'),
        'file_name': ('-r', '--read_from_file')

    }

    callsign: str = ''
    raw_tags: str = ''
    invited_by: str = ''

    creation_time: int = get_time()
    modification_time: int = creation_time
    id_value: str = generate_id()

    source: dict[str | Any, int | str | object | float | Any] = {
        '_source_schema_version': SOURCE_SCHEMA_VERSION,
        'callsign':     callsign,
        'tags':         raw_tags,
        'invited_by':   invited_by,
        'id':           id_value,
        'type':         set_type(),
        'reliability':  4.98,
        'note':         'some new note',
        'created':      creation_time,
        'modified':     modification_time,
        'invite':       generate_invite(),
        'stats': {
            'total facts':      0,
            'confirmed facts':  0,
            'refuted facts':    0
        }
    }

    opts: list[tuple[str, str]] = parse_input_options(sys.argv[3:])
    # print(type(opts), opts)

    for key, value in opts.items():
        for map_key, map_value in option_map.items():
            if key in map_value:
                source[map_key] = value
                break

    raw_tags = source['tags']
    source['tags'] = extract_tags(raw_tags)

    for key, value in source.items():
        print(f'{key}: {value}')

    filename: str = PATH_TO_STORAGE + id_value + EXTENSION
    save_to_yaml(source, filename)
