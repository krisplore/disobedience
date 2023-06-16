import datetime
import getopt
import sys
import uuid
import yaml
import secrets
import string

EXTENSION = '.yaml'
AMOUNT_OF_INVITATIONS = 2
INVITATION_LENGTH = 6


def extract_tags(tags):  # tags!  а что если запятой нет defensive programming
    tags = [item.strip() for item in tags.split(',') if item.strip()]
    return tags


def generate_id():
    return str(uuid.uuid4())


def set_type():
    return 1


def generate_invite(amount, length):
    alphabet = string.ascii_uppercase + string.digits
    excluded_characters = 'IiOo01l'
    characters = [c for c in alphabet if c not in excluded_characters]
    invite = []
    for _ in range(amount):
        invite.append(''.join((secrets.choice(characters) for _ in range(length))))
    return invite


def get_time():
    return int(datetime.datetime.now().timestamp())


def main(argv):
    callsign = ''
    tags = ''
    invited_by = ''

    try:
        opts, args = getopt.getopt(argv, 'c:t:i:', ['callsign=$', 'tags=$', 'invited_by=$'])
    except getopt.GetoptError:  # работает только если тэги в кавычках поступают
        print('There is something wrong with arguments')
#        sys.exit(2)   # код возврата 2 - некорректный аргумент командной строки

    for opt, arg in opts:
        if opt in ('-c', '--callsign'):
            callsign = arg  #
        elif opt in ('-t', '--tags'):
            tags = arg
        elif opt in ('-i', '--invited_by'):
            invited_by = arg

    tags_list = extract_tags(tags)
    id_str = generate_id()
    type_int = set_type()
    creation_time_str = get_time()
    modification_time_str = creation_time_str
    invitations = generate_invite(AMOUNT_OF_INVITATIONS, INVITATION_LENGTH)

    source = {
        'callsign': callsign,
        'tags': tags_list,
        'invited_by': invited_by,
        'id': id_str,
        'type': type_int,
        'reliability': 4.98,
        'note': 'some new note',
        'created': creation_time_str,
        'modified': modification_time_str,
        'invite': invitations,
        'stats': {
            'total_facts': 0,
            'confirmed_facts': 0,
            'refuted_facts': 0
        }
    }

    print(source)

    filename = 'data/source/' + source['id'] + EXTENSION
    with open(filename, 'w') as file:
        yaml.dump(source, file)


if __name__ == "__main__":
    main(sys.argv[1:])



