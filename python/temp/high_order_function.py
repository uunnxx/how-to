def twice(f):
    print(f'{f=}')

    def result(x):
        print(f'{x=}')
        # x=7, f(i) - it's lambda i: i+3... x to lambda and lambda will return 7+3 = 10, x=10
        # print(f(x))
        # x=7, lambda return 7+3=10, so x=10, lambda return 10+3=13, x=13
        # print(f(f(x)))
        # x=7, lambda return 7+3=10, x=10, lambda return 10+3=13, x=13 lambda return 13+3=16, x=16
        # print(f(f(f(x))))
        return f(f(x))
    return result

# plus_three = lambda i: i + 3
#
# g = twice(plus_three)
#
# print(g(7))


@twice
def gg(i):
    return i + 3


print(f'{gg(7)=}')
