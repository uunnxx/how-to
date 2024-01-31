colors = ['black', 'white']
sizes = ['S', 'M', 'L']

tshirts = [
    (color, size)
    for color in colors
    for size in sizes
]

# print(tshirts)

# for color in colors:
#     for size in sizes:
#         print((color, size))

import os
_, filename = os.path.split('/home/baka/.ssh/forcodeberg.pub')
# print(_)
# print(filename)

board = [['_'] * 3 for _ in range(3)]
board = [['_'] * 3 ] * 3  # three references to the same list

# print(board)


lst: list = [28, 14, '28', 5, '9', '1', 0, 6, '23', 19]

# lst_sorted = sorted(list(map(int, lst)))

# print(lst_sorted)

# print(sorted(lst, key=int))


def get_creators(record: dict) -> list:
    match record:
        case {'type': 'book', 'api': 2, 'authors': [*names]}:
            return names
        case {'type': 'book', 'api': 1, 'authors': [name]}:
            return [name]
        case {'type': 'book'}:
            raise ValueError(f"Invalid 'book' record: {record!r}")
        case {'type': 'movie', 'director': name}:
            return [name]
        case _:
            raise ValueError(f'Invalid record {record!r}')


# food = dict(category='ice cream', flavor='vanilla', cost=199)
# match food:
#     case {'category': 'ice cream', **details}:
#         print(f'Ice cream details: {details}')


from collections import abc

# my_dict = {}
# isinstance(my_dict, abc.Mapping)
# isinstance(my_dict, abc.MutableMapping)


# class CustomList:
#     def __init__(self, lst: list[int]):
#         self.lst: list = lst
#
#     # def __getitem__(self, index):
#     #     if 0 < index <= len(self.lst):
#     #         return self.lst[index]
#
#     def __getitem__(self, item):
#         if item in self.lst:
#             return self.lst.index(item)
#
#     def __missing__(self, missing_item):
#         print(f'<missing> {missing_item}...')
#
#
# a = CustomList([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
#
# print(a[21])




class CustomDict(dict):
    def __init__(self, lst: dict):
        self.dct = lst

    def __missing__(self, missing_item):
        print(f'<missing> {missing_item}...')
        # try:
        #     return super().__missing__(missing_item)
        # except AttributeError:
        #     raise KeyError(missing_item)

    # def __getitem__(self, item):
    #     if item in self.dct:
    #         return self.dct.get(item)



my_dict = CustomDict({'Alice': 23, 'Bob': 24, 'Carl': 25})

print(my_dict['Alice'])
# print(my_dict['Joe'])
