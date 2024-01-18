import json


d = {'a': 3, 'b': 3, 'c': 12}
res = json.dumps(d)

print(res)


d = {'a': True, 'b': False, 'c': True}
d_json = json.dumps(d)
print(d_json)


print(json.loads(d_json))

persons = {
    'Isabella': {
        'surname': 'Jones',
        'address': ('Bright Av.', 34, 'Village of Sun')
    },
    'Noah': {
        'surname': 'Horton',
        'address': (None, None, 'Whoville')
    }
}

persons_json = json.dumps(persons)

print(persons_json)
