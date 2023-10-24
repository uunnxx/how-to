def br(delimiter='-', width=80) -> None:
    print(f'\n{delimiter * width}')


a: int = 10
b: float = float(10)


print(f'{a} >> {type(a)}\n{b} >> {type(b)}')


a, b, c = 5, 6.4, 'String'

print(a, b, c)

print(f'{type(a)} :: {type(a)} :: {type(a)}')


t = (10, )

print(type(t))


my_set = {1, 2, 3, 4, 5}
my_set2 = {'apple', 'banana', 'cherry'}

print(type(my_set))
print(type(my_set2))

my_list: list = [i for i in range(1, 6)]
print(my_list)


br()
