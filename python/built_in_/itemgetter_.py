from operator import itemgetter


items: dict[str, int] = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
elements: dict[str, int] = {'a': 100, 'b': 200, 'c': 300}

a_and_c: itemgetter = itemgetter('a', 'c')

print(a_and_c(items))
print(a_and_c(elements))
