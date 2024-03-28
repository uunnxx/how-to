dct = {
    # 'key': 'value'
    'key0': 0,
    'key1': 5,
    'akey1': 5,
    'bkey1': 5,
    'key2': 1,
    'key3': 8,
    'key4': 9,
    'key5': 4
}


for i in sorted(dct.items(), key=lambda el: (el[1], el[0])):
    print(i)
