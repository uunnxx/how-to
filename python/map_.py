numbers: list[int] = [i for i in range(1, 7)]


def convert_to_str(element):
    return str(element)


converted_list: list[str] = list(map(convert_to_str, numbers))


print(converted_list)
