import sys              #
import os
import gettext          # translate the strings
import yaml             # write dict source to yaml file
from lib.command_line_parser import parse_command_line
from lib.functions import get_time, extract_tags, generate_id, generate_invite, set_type


_ = None
EXTENSION = '.yaml'
PATH_BASE = '.'
PATH_TO_LOCALES = PATH_BASE + '/locales'
PATH_TO_STORAGE = PATH_BASE + 'data/source/'
NAME_PROJECT = 'disobedience'


def main():
    global _
    language = gettext.translation(NAME_PROJECT, localedir=PATH_TO_LOCALES)
    language.install()
    _ = language.gettext

    print(_("Language"))

    option_map = {
        'callsign': ('-c', '--callsign'),
        'tags': ('-t', '--tags'),
        'invited by': ('-i', '--invited_by')

    }

    callsign = ''
    raw_tags = ''
    invited_by = ''

    creation_time = get_time()
    modification_time = creation_time
    id_value = generate_id()

    source = {
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

    options = {}
    for opt, arg in opts:
        dictionary_key = option_map.get(opt)
        if dictionary_key:
            options[dictionary_key] = arg

    source['tags'] = extract_tags(raw_tags)

    for key, value in source.items():
        print(f'{key}: {value}')

    filename = PATH_TO_STORAGE + id_value + EXTENSION
    with open(filename, 'w') as file:
        yaml.dump(source, file)


if __name__ == "__main__":
    main()