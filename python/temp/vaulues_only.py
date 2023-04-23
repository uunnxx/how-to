def values_only(dict):
    return [v for k, v in dict.items()]


ages = {
    'Peter': 10,
    'Isabel': 11,
    'Anna': 9
}


print(values_only(ages))
