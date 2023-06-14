import yaml
import uuid
import datetime
id = str(uuid.uuid4())
callsign = input()
category = int(input())  # type
reliability = float(input())
note = input()
tegs = input()
invited_by = input()
invite = uuid.uuid4(), uuid.uuid4()
created = datetime.datetime.now().time().strftime('%H:%M:%S')
modified = ''
fact = input()
    # 'Verified':
    # 'Total':
    # 'False_facts':

 #       'id' # GUID
  #      'source': "ewf"  # GUID
   #     'created': datetime(2023, 6, 12, 15, 33, 0),
    #    'description': 'Military detachment spotted',
   #    'happened'
   #     'location': '20.858659, 96.052031', # словарь широта и долгота, высота
   #         'address'
   #         'note' # 3 этаж допустим
   #     'corrobaration': 4,
   #     'corrobarated_by':
   #     'modified'


