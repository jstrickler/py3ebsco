#!/usr/bin/env python
import re
from pymongo import MongoClient

FIELD_NAMES = (
    'termnumber lastname firstname '
    'birthdate '
    'deathdate birthplace birthstate '
    'termstartdate '
    'termenddate '
    'party'
).split() # <1>

mc = MongoClient() # <2>

try:
    mc.drop_database("presidents") # <3>
except:
    pass

db = mc["presidents"] # <4>

coll = db.presidents  # <5>

with open('../DATA/presidents.txt') as PRES: # <6>
    for line in PRES:
        flds = line[:-1].split(':')
        kvpairs = zip(FIELD_NAMES, flds)
        record_dict = dict(kvpairs)
        coll.insert(record_dict)  # <7>

print(db.collection_names())  # <8>
print()

abe = coll.find_one({'termnumber': '16'})  # <9>
for field in FIELD_NAMES:
    print("{0:15s} {1}".format(field.upper(), abe[field])) # <10>
    
print('-' * 50)

for president in coll.find(): # <11>
    print("{0[firstname]:25s} {0[lastname]:30s}".format(president))
print('-' * 50)

rx_lastname = re.compile('^roo', re.IGNORECASE)
for president in coll.find({ 'lastname': rx_lastname }): # <12>
    print("{0[firstname]:25s} {0[lastname]:30s}".format(president))
print('-' * 50)

for president in coll.find({"birthstate": 'Virginia',  'party': 'Whig'}): # <13>
    print("{0[firstname]:25s} {0[lastname]:30s}".format(president))
    
print('-' * 50)
print("removing Millard Fillmore")
result = coll.remove({'lastname': 'Fillmore'})  # <14>
print(result)
result = coll.remove({'lastname': 'Roosevelt'}) # <14>
print(result)
print('-' * 50)
result = coll.count()  # <15>
print(result)
