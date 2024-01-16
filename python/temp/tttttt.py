import json
from datetime import datetime


def br():
    print(f'\n{'-' * 80}\n')


br()


def careful_divide(x: int | float, y: int | float) -> int | float:
    """
    Divides x by y.

    Raises:
        ValueError: When the inputs cannot be divided.
    """
    try:
        return x / y
    except ZeroDivisionError:
        raise ValueError('Invalid Inputs')


# x, y = 5, 2
x, y = 4, 0

try:
    result = careful_divide(x, y)
except ValueError:
    print('Invalid Inputs')
else:
    print(f'Result is {result:.1f}')


def sort_priority(values, group):
    def helper(x):
        if x in group:
            return (0, x)
        return (1, x)
    values.sort(key=helper)


numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}

sort_priority(numbers, group)
print(numbers)


def sort_priority2(numbers, group):
    found = False

    def helper(x):
        if x in group:
            nonlocal found
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found


class Sorter:
    def __init__(self, group):
        self.group = group
        self.found = False

    def __call__(self, x):
        if x in self.group:
            self.found = True
            return (0, x)
        return (1, x)


sorter = Sorter(group)
numbers.sort(key=sorter)
assert sorter.found is True


def log(message, *values):
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print(f'{message}: {values_str}')


log('My numbers are', [1, 2])
log('Hi there', [])
log('Hi there')


def my_generator():
    for i in range(10):
        yield i

def my_func(*args):
    print(args)


it = my_generator()
my_func(*it)

br()

def log2(sequence, message, *values):
    if not values:
        print(f'{sequence} - {message}')
    else:
        values_str = ', '.join(str(x) for x in values)
        print(f'{sequence} - {message}: {values_str}')


log2(1, 'Favorites', 7, 33)
log2(1, 'Hi there')
log2('Favorite numbers', 7, 33)




br()

def remainder(number, divisor):
    return number % divisor


assert remainder(20, 7) == 6


def decode(data, default=None):
    '''
    Load JSON data from a string.

    Args:
        data: JSON data to decode.
        default: Value to return if decoding fails.
            Defaults to an empty dictionary.
    '''
    try:
        return json.loads(data)
    except ValueError:
        if default is None:
            default = {}

        return default


foo = decode('bad data')
foo['stuff'] = 5
bar = decode('also bad data')
bar['meep'] = 1
print('Foo:', foo)
print('Bar:', bar)
assert foo is not bar


from typing import Optional


def log_typed(message: str,
              when: Optional[datetime] = None) -> None:
    '''
    Log a message with a timestamp.

    Args:
        message: Message to print.
        when: datetime of when the message occurred.
            Default to the present time.
    '''
    if when is None:
        when = datetime.now()
    print(f'{when}: {message}')


log_typed('Log Message')


def save_division(number, divisor,
                  ignore_overflow=False,
                  ignore_zero_division=False):

    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise


result = save_division(1.0, 10**500, True, False)
print(result)  # 0

result = save_division(1.0, 0, True, False)
print(result)  # inf
