def calc(num1: int | float = 0, num2: int | float = 0) -> int | float:
    '''Takes two numbers and returns it\'s sums'''
    return num1 + num2


# print(type(calc(2.5)))
# print(calc(1, 2.5))
#
#
# print(calc.__doc__)
#
#
# def outer_fn(num1: int | float, num2: int | float) -> int | float:
#     def inner_fn(n1, n2):
#         return n1 + n2
#     total = inner_fn(num1, num2)
#     return total
#
#
# print(outer_fn(2, .5))
# print(type(outer_fn(2, .5)))

# print(help(calc))

# def addition(*args):
#     print(sum(args))
#     print(*args)
#
#
# addition(2, 2, 2)


def addition(*args, **kw):
    print(sum(args) + sum(kw.values()))
    # print(sum(kw.values()))
    # print(*args)


addition(2, 2, 2, n=4)


import time


class Ticket:
    def __init__(self, date, name, deadline):
        self.create_date = date
        self.owner = name
        self.deadline = deadline

    def __del__(self):
        print(f"Delete ticket: {time.asctime(self.create_date)}")

    def display(self):
        pass

# t = Ticket(date, name, datetime)



