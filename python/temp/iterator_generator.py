def br():
    print()
    print('-' * 80)
    print()


a = tuple(range(1, 12))

print(a)
print(type(a))

for i in range(1, 10, 2):
    print(i)

br()


def thisistech(string):
    '''
    Yield reverse string
    '''
    tech = len(string)
    for k in range(tech - 1, -1, -1):
        yield string[k]


for char in thisistech('whassup'):
    print(char)

br()

myfirstline = [1, 10, 9, 0]
listmy = [k**2 for k in myfirstline]
generator = (k**2 for k in myfirstline)

print(listmy)
print(generator)

br()

mysecondlist = [1, 10]
p = (j**2 for j in mysecondlist)
print(next(p))
print(next(p))

br()

print(sum(w**2 for w in mysecondlist))


# Comparison Between Python Generator and Iterator
# | S.no  | Parameters            | Generator                                                     | Iterator                                                                              |
# | 1     | Implementation        | Implemented using a function defined in the runtime.          | Implemented using a class in the code.                                                |
# | 2     | Yield usage for coder | Generator uses the ‘yield’ keyword                            | Iterator does not use any keyword                                                     |
# | 3     | Class variable        | Generator does not need a class in python.                    | Iterator implements its own class                                                     |
# | 4     | Globals and locals    | Generator saves the states of the local variables             | Iterator also does not uses local variable                                            |
# | 5     | Yield usage for user  | Uses the yield keyword for the output.                        | Does not use the yield keyword anywhere in the code.                                  |
# | 6     | Efficiency            | Generators  write fast and compact code                       | Iterator writes custom and long codes                                                 |
# | 7     | Functions             | Generator use python functions                                | Iterator,use the iter() and next() functions                                          |
# | 8     | Storage capacity      | Generator is not memory efficient                             | Iterator is memory-efficient                                                          |
# | 9     | Relative working      | Usage results in a concise code in any relative function.     | Usage results in a relatively less concise code as compared in the whole python code. |

br()


def string(my_string):
    length = len(my_string)
    for i in range(length):
        yield my_string[i]

def string2(my_string):
    yield from my_string

for string in 'python':
    print(string)

br()

for ch in string2('python'):
    print(ch)

br()


# Generator
class fibonacci:
    def __init__(self, num):
        self.num = num
        self.num1, self.num2 = 2, 3

    def __iter__(self):
        for _ in range(self.num):
            yield self.num1
            self.num1, self.num2 = self.num2, self.num1 + self.num2

f = fibonacci(3)

for i in f:
    print(i)

br()


class EvenNumbers:
    def __iter__(self):
        self.a = 2
        return self

    def __next__(self):
        numbers = self.a
        self.a += 2
        return numbers

myclass = EvenNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

br()


def common_divisors_generator(a):
    factors_a = [i for i in range(2, a+2) if a % i == 0]
    def gen():
        yield from factors_a

    return gen()
print(common_divisors_generator)
