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
























