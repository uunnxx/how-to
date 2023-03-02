def square(x):
    print(x * x)

def cube(x):
    print(x**3)

def quartic(x):
    print(x**4)


# power_two = square
# power_two(6)


powers = [square, cube, quartic]
# powers[2](5)

[calculate(6) for calculate in powers]


def decorator_function(func):
    '''A function that accepts another function'''
    def wrapper():
        print('wrapping')
        func()
        print('done')
    return wrapper


def f():
    '''Example function'''
    print('function f called')

decorator = decorator_function(f)
print(decorator)
decorator()  # the inner wrapper function is returned so it needs to called

