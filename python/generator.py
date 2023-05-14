# Generator Delegation

# Python 3.3 introduced `yield` from expression. It allows a generator to delegate parts of operations to another generator.
# In other words, we can `yield` a sequence `from` other `generators` in the `generator function`.
# Further information can be found on PEP 380.

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        b, a = a + b, b


def fibonacci(n):
    yield from fib(n)

print([f for f in fib(5)])

print([f for f in fibonacci(5)])


class A:
    pass

class B:
    pass

class Foo(A, B):
    '''A class document.'''

    foo = 'class variable'

    def __init__(self, v):
        self.attr = v
        self.__private = 'private var'

    @staticmethod
    def bar_static_method(cls):
        pass

    def bar(self):
        '''A method document.'''

    def bar_with_arg(self, arg):
        pass
    

