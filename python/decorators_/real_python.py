# Decorators
# What is a decorator?
# - A function that takes another function
# - Extends the behavior of that function
# - Without explicitly modifying the function


# Functions
# - Header
# - Statement
# - Calling the Function



def br():
    print(f'\n{"-" * 80}\n')


def my_function():
    """docstring"""
    pass


my_function()


def my_function2(argument):
    """docstring"""
    my_var = argument * 5
    return my_var


def add_one(number: int) -> int:
    """A function that adds one to the given number and returns it"""
    result = number + 1
    print(result)
    return result


add_one(3)  # 4
add_one(9)  # 10


add_one_also = add_one

add_one_also(3)  # 4
add_one_also(9)  # 10


print(add_one_also == add_one)


# Functions are First-Class objects


def say_hello(name: str):
    return f'Hello {name}'


say_hello('Chris')


def be_awesome(name: str):
    return f'Yo {name}, together we are the awesomest!'


be_awesome('Gregor')


my_list = [say_hello, be_awesome]

my_list[0]('Chris')


def greet_bob(greeter_func):
    return greeter_func('Bob')


greet_bob(say_hello)

br()


# Inner Functions

def parent():
    print('Print from the parent() function')

    def first_child():
        print('Printing from the first_child() function')

    def second_child():
        print('Printing from the second_child() function')
        
    second_child()
    first_child()


parent()

br()

# Returning Functions from Functions

def parent2(num):
    def first_child():
        print('Hi, I am Emma')

    def second_child():
        print('Call me Liam')
        
    if num == 1:
        return first_child
    # else:
    #     return second_child
    return second_child
    second_child()
    first_child()


first = parent2(1)
second = parent2(2)
first()
second()


br()


print(first)
print(second)


br()


# Decorators

## Simple Decorators

def my_decorator(func):
    def wrapper():
        print('Something is happening before the funciton is called.')
        func()
        print('Something is happening after the funciton is called.')

    return wrapper


def say_whee():
    print('Whee!')


say_whee = my_decorator(say_whee)


print(say_whee)

br()

say_whee()


br()


from datetime import datetime

def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass

    return wrapper


def say_whee2():
    print('Whee!')


say_whee2()

# say_whee2 = not_during_the_night(say_whee2)
not_during_night_whee = not_during_the_night(say_whee2)




say_whee2()


br()


# Syntactic Sugar

def my_decorator2(func):
    def wrapper():
        print('Something is happening before the funciton is called.')
        func()
        print('Something is happening after the funciton is called.')

    return wrapper


@my_decorator2
def say_whee3():
    print('Whee!')


# say_whee3 = my_decorator2(say_whee3)
# say_whee3()
say_whee3()

br()


# Reusing Decorators

from decs import decorators as dec

@dec.do_twice
def say_whee4():
    print('Whee!')


say_whee4()

br()


# Decorator Functions weth Arguments


# @dec.do_twice
# def greet(name):
#     print(f'Hello {name}')


# greet('Liam') ## TypeError


@dec.do_twice_with_one_arg
def greet(name):
    print(f'Hello {name}')


greet('Liam')


br()

# Returning values from Decorated Functions


import time

@dec.timer
def slow_code():
    print('Running')
    time.sleep(2)
    print('Finished')


@dec.timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10_000)])



# slow_code()
# br()


waste_some_time(2)

br()

@dec.debug
def make_greeting(name: str, age: int = None):
    name = name.capitalize()
    if age is None:
        return f'Howdy {name}!'
    return f'Whoa {name}! {age} already, you are growing up!'


make_greeting('john')
make_greeting('john', age=30)


br()


import math


math.factorial = dec.debug(math.factorial)

def approximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))


approximate_e(3)

br()

@dec.slow_down
def countdown(from_number):
    if from_number < 1:
        print('Liftoff!')
    else:
        print(from_number)
        countdown(from_number - 1)


# countdown(10)
# br()


print(dec.register)


@dec.register
def say_hello2(name):
    return f'Hello {name}'


@dec.register
def be_awesome2(name):
    return f'Yo {name}, together we are the awesomest!'


print(dec.PLUGINS)

br()

import random


def randomly_greet(name):
    greeter, greeter_func = random.choice(list(dec.PLUGINS.items()))
    print(f'Using {greeter!r}')
    print(greeter_func(name))


randomly_greet('Alice')


# links:
#     https://stackoverflow.com/questions/5929107/decorators-with-parameters
#     https://www.youtube.com/watch?v=MjHpMCIvwsY
