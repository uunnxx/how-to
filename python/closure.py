# def main_func():
#     name = 'Ivan'
#     def inner_func():
#         print('hello my friend', name)
#
#     # inner_func()
#     return inner_func

# main_func()

# a = main_func()
# a()
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

def main_func(value):
    name = value
    def inner_func():
        print('hello my friend', name)

    # inner_func()
    return inner_func


# r = main_func('Baaka')
# r()


# v = main_func('Ande')
# v()

# -----------------------------------------------------------------------------

def adder(value):

    def inner(a):
        return value + a

    return inner

# add = adder(10)
# print(add(2))

# -----------------------------------------------------------------------------

def counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

count = counter()
print(count())
print(count())
print(count())
print(count())
print(count())
print(count())

# -----------------------------------------------------------------------------


numbers = []
def enter_number(x: int) -> None:
    numbers.append(x)
    print(numbers)


enter_number(3)
enter_number(4)
enter_number(5)


# For modularity, if we want to use somewhere else this function,
# we need to move global `numbers` variable, too.


# Use closure for this purpose


def enter_number_outer():
    numbers = []
    def enter_number_inner(x: int):
        numbers.append(x)
        print(numbers)
    return enter_number_inner


enter_num = enter_number_outer()

enter_num(3)
enter_num(4)
enter_num(5)


class enter_number_outer():
    numbers = []
    def enter_number_inner(self, x):
        self.numbers.append(x)
        print(self.numbers)
