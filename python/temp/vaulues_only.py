def values_only(dict):
    lst = []
    for k, v in dict.items():
        lst.append(v)
    return lst


ages = {
    'Peter': 10,
    'Isabel': 11,
    'Anna': 9
}


print(values_only(ages))
