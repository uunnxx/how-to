def f():
    return 4 / 0

def g():
    raise Exception("Don't call us. We'll call you")

def h():
    try:
        f()
    except Exception as e:
        print(e)
    try:
        g()
    except Exception as e:
        print(e)

h()


# RAISING EXCEPTIONS

# Raise an instance of the Exception class itself
raise Exception('Ummmm... something is wrong')

# Raise an instance of the RuntimeError class
raise RuntimeError('Ummm... something is wrong')

# Raise a custom subclass of Exception that keeps the timestamp the exception
# was created
from datetime import datetime

class SuperError(Exception):
    def __init__(self, message):
        Exception.__init__(message)
        self.when = datetime.now()

raise SuperError('Ummm... something is wrong')


# CATCHING EXCEPTIONS

# You catch exceptions with that `except` clause, as you saw in the example,
# Consider the example below:
while True:
    try:
        x = int(input('Please enter a number: '))
    except ValueError:
        print('Opps! That was no valid number. Try again...')


# SWALLOW THE EXCEPTION

import json
import yaml


def parse_file(filename):
    try:
        return json.load(open(filename))
    except json.JSONDecodeError:
        return yaml.load(open(filename))


# If you want to handle all exceptions then just use
# `except Exception`. For example:

def print_exception_type(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as e:
        print(type(e))

# Note that by adding `as e`, you bind the exception object to the name `e`
# available in your except clause.

# RAISE THE SAME EXCEPTION AGAIN

def invoke_function(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as e:
        print(type(e))
        raise



# BaseException
#  +-- SystemExit
#  +-- KeyboardInterrupt
#  +-- GeneratorExit
#  +-- Exception
#       +-- StopIteration
#       +-- StandardError
#       |    +-- BufferError
#       |    +-- ArithmeticError
#       |    |    +-- FloatingPointError
#       |    |    +-- OverflowError
#       |    |    +-- ZeroDivisionError
#       |    +-- AssertionError
#       |    +-- AttributeError
#       |    +-- EnvironmentError
#       |    |    +-- IOError
#       |    |    +-- OSError
#       |    |         +-- WindowsError (Windows)
#       |    |         +-- VMSError (VMS)
#       |    +-- EOFError
#       |    +-- ImportError
#       |    +-- LookupError
#       |    |    +-- IndexError
#       |    |    +-- KeyError
#       |    +-- MemoryError
#       |    +-- NameError
#       |    |    +-- UnboundLocalError
#       |    +-- ReferenceError
#       |    +-- RuntimeError
#       |    |    +-- NotImplementedError
#       |    +-- SyntaxError
#       |    |    +-- IndentationError
#       |    |         +-- TabError
#       |    +-- SystemError
#       |    +-- TypeError
#       |    +-- ValueError
#       |         +-- UnicodeError
#       |              +-- UnicodeDecodeError
#       |              +-- UnicodeEncodeError
#       |              +-- UnicodeTranslateError
#       +-- Warning
#            +-- DeprecationWarning
#            +-- PendingDeprecationWarning
#            +-- RuntimeWarning
#            +-- SyntaxWarning
#            +-- UserWarning
#            +-- FutureWarning
#   +-- ImportWarning
#   +-- UnicodeWarning
#   +-- BytesWarning

