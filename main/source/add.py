import sys              #
import gettext          # translate the strings
from lib.input.getopt_input import parse_command_line
from lib.process.functions import get_time, extract_tags, generate_id, generate_invite, set_type
from pathlib import Path
from lib.process.save_to_yaml import save_to_yaml


_ = None
EXTENSION = '.yaml'
PATH_BASE = Path(__file__).parent.parent.__str__()
PATH_TO_LOCALES = PATH_BASE + '/locales'
PATH_TO_STORAGE = PATH_BASE + '/data/source/'
NAME_PROJECT = 'disobedience'
_SOURCE_SCHEMA_VERSION = 1


def main():
    global _
    print(PATH_BASE)
    language = gettext.translation(NAME_PROJECT, localedir=PATH_TO_LOCALES)
    language.install()
    _ = language.gettext

    print(_("Language"))

    option_map = {
        'callsign': ('-c', '--callsign'),
        'tags': ('-t', '--tags'),
        'invited_by': ('-i', '--invited_by'),
        'file_name': ('-r', '--read_from_file')

    }

    callsign = ''
    raw_tags = ''
    invited_by = ''
    file_name = ''

    creation_time = get_time()
    modification_time = creation_time
    id_value = generate_id()

    source = {
        '_source_schema_version': 1,
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

    opts = parse_command_line(sys.argv[1:])
    print(type(opts), opts)

    for key, value in opts.items():
        for map_key, map_value in option_map.items():
            if key in map_value:
                source[map_key] = value
                break

    raw_tags = source['tags']
    source['tags'] = extract_tags(raw_tags)

    for key, value in source.items():
        print(f'{key}: {value}')

    filename = PATH_TO_STORAGE + id_value + EXTENSION
    save_to_yaml(source, filename)


if __name__ == "__main__":
    main()