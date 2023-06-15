import datetime
import getopt
import re
import sys
import uuid
import yaml
import gettext

EXTENSION = '.yaml'
NUMBER_INVITE = 2  # вынести и переименовать


def set_id():  #
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, 'disobedience'))


def set_type():
    return 1


def set_invite():  #
    invite = []
    for _ in range(NUMBER_INVITE):
        invite.append(str(uuid.uuid4()))  # 6 англ символов и цифр без спорных uppercase
    return invite


def set_tags(tags):  # tags!
    tags = tags.split(',')  # а что если запятой нет defensive programming
    tags = [re.sub(r'\s+', ' ', item.strip()) for item in tags]  # убрать re
    return tags


def main(argv):
    callsign = ''
    tags = []
    invited_by = ''

    try:
        opts, args = getopt.getopt(argv, 'c:t:i:', ['callsign=', 'tags=', 'invited_by='])
    except getopt.GetoptError:  #
        print('There is something wrong with arguments')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-c', '--callsign'):
            callsign = arg      #
        elif opt in ('-t', '--tags'):
            tags = arg
        elif opt in ('-i', '--invited_by'):
            invited_by = arg

    source = {}
    source['callsign'] = callsign
    source['tags'] = tags
    source['invited_by'] = invited_by

    source['id'] = set_id()
    source['type'] = set_type()
    source['reliability'] = 4.98
    source['tags'] = set_tags(tags)
    source['note'] = 'some new note'
    source['invite'] = set_invite()
    source['created'] = int(datetime.datetime.now().timestamp())
    source['modified'] = source['created']
    # source['stats'] = [
    #     'facts' = [
    #         'total' = 0
    #     ]
    # ]

    print(source)

    filename = source['id'] + EXTENSION
    with open(filename, 'w') as file:
        yaml.dump(source, file)


if __name__ == "__main__":
    main(sys.argv[1:])
