import uuid
import datetime

def set_id():
    return str(uuid.uuid5(uuid.NAMESPACE_OID, callsign))

def set_type():
    return 1

def set_invite():
    NUMBER_INVITE = 2
    invite = []
    for i in range(NUMBER_INVITE):
        invite.append(str(uuid.uuid4()
    return invite

def set_tegs(tegs):
    tegs_array = tegs.split(',')
    tegs_array = [item.strip() for item in tegs_array]
    return tegs_array


source = {}
user_key = ['callsign', 'tegs', 'invited_by']


for key in user_key:
    answer = input(f'Enter answer for item {key}:  ')
    source[key] = answer

callsign = source['callsign']
tegs = source['tegs']
print(type(tegs))
source['id'] = set_id()
source['type'] = set_type()
source['reliability'] = 4.98
source['tegs'] = set_tegs(tegs)
source['note'] = 'some new note'
source['invite'] = set_invite()
source['created'] = datetime.datetime.now().time().strftime('%H:%M:%S')
source['modified'] = source['created']
source['fact'] = []


print(source)

