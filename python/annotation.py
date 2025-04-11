def foo(a, b, c: int) -> float:
    return (a + b + c)

# foo('Hello', ', ', 'World!')
foo(1, 2, 3)


def foo2(x = 5):
    print(x)

foo2(7)

foo2()


print(foo.__annotations__)


def bar(*args, **kwargs: 'the keyword arguments dict'):
    print(kwargs['return'])


d = {'return': 4}
bar(**d)

print(bar.__annotations__)


def div(a, b):
    """
Divide a by b args:
    a - the dividend
    b - the divisor (must be different than 0)
    return: the result of dividing a by b
    """
    return a / b

print(div.__doc__)


print(dir(div))

print('-' * 80)
print(help(div))
