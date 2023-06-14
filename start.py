import uuid
import datetime

def set_id_fact():
    return str(uuid.uuid5(uuid.NAMESPACE_OID, description))

def set_created():
    return datetime.datetime.now().time().strftime('%H:%M:%S')


fact = {}
user_key = ['description', 'happened']
location_keys = ['latitude', 'longitude', 'height', 'locality', 'address', 'note']

for key in user_key:
    fact[key] = input(f'Enter answer for item {key}:  ')

location = {}
for key in location_keys:
    location[key] = input(f'Enter answer for item {key}:  ')

description = []
fact['location'] = location
source = 'John' # link for the dict_sourse file
id_fact = set_id_fact()
created = set_created()
modified = created
corrobarated_by = []
corrobaration = len(corrobarated_by)
