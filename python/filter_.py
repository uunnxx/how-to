people: list[str | int] = ['Mario', 'Luigi', 10, 'Toad', 20]


def is_str(element):
    return isinstance(element, str)

def is_int(element):
    return isinstance(element, int)

filtered_people: list[str] = list(filter(is_str, people))
filtered_integers: list[str] = list(filter(is_int, people))


print(filtered_people)
print(filtered_integers)
