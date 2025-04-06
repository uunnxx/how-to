from functools import reduce
import time
import os
from datetime import datetime
import itertools
import heapq
from typing import Callable, ParamSpec, TypeVar, override
import datetime as dt
fizz_buzz_squares: list[int] = []

for num in range(10):
    if (num % 3 == 0) or (num % 5 == 0):
        fizz_buzz_squares.append(num**2)


fizz_buzz_squares2 = [num**2 for num in range(10) if (num % 3 == 0) or (num % 5 == 0)]


def get_aws_prefixes() -> list[str]:
    return ["first", "second", "third"]


def get_service_prefixes(amazon_service):
    service_prefixes: list[str] = [
        prefix for prefix in get_aws_prefixes() if amazon_service in prefix["service"]
    ]

    count: int = len(service_prefixes)
    return count


class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.name = f"{self.first} {self.last}"


# john = Person('John', 'Doe')
# print(john.name)
# john.last = 'Smith'
# print(john.name)


class Person1:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.name = f"{self.first} {self.last}"

    def set_first(self, first):
        self.first = first
        self.name = f"{self.first} {self.last}"

    def set_last(self, last):
        self.last = last
        self.name = f"{self.first} {self.last}"


# john = Person1('John', 'Doe')
# print(john.name)
# john.set_first('Smith')
# print(john.name)


class Person2:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def get_name(self):
        return f"{self.first} {self.last}"


# john = Person2('John', 'Doe')
# print(john.get_name())
# john.first = 'Smith'
# print(john.get_name())
# john.last = 'Rog'
# print(john.get_name())


class Person3:
    def __init__(self, first: str, last: str):
        self.first: str = first
        self.last: str = last

    @property
    def name(self):
        return f"{self.first} {self.last}"


# john = Person3('John', 'Doe')
# print(john.name)
#
# john.first = 'Smith'
# print(john.name)
#
# john.last = 'Rogger'
# print(john.name)


class Person4:
    def __init__(self, first, last, birthday):
        self.first = first
        self.last = last
        self.birthday = birthday

        today = dt.date.today()
        current_year = today.year

        # Will the preson still celebrate their birthday tihs current year?
        will_celebrate = birthday.replace(year=current_year) > today
        self.age = current_year - birthday.year - will_celebrate

    @property
    def name(self):
        return f"{self.first} {self.last}"


class Person5:
    def __init__(self, first, last, birthday):
        self.first = first
        self.last = last
        self.birthday = birthday

    @property
    def age(self):
        today = dt.date.today()
        current_year = today.year

        # Will the preson still celebrate their birthday tihs current year?
        will_celebrate = birthday.replace(year=current_year) > today

        return current_year - self.birthday.year - will_celebrate

    @property
    def name(self):
        return f"{self.first} {self.last}"


# class PurePath:
#     # ...
#
#     @property
#     def name(self):
#         '''The final path component, if any.'''
#         print('Computing the name!')
#         parts = self._parts
#         if len(parts) == (1 if (self._drv or self._root) else 0):
#             return ''
#
#         return parts[-1]
#


class Colour:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

        self.rgb = (r, g, b)

    @property
    def hex(self):
        return "#%02x%02x%02x" % self.rgb


c = Colour(146, 255, 122)
# print(c.hex)


class Colour1:
    def __init__(self, hex_string):
        self.hex = hex_string

    @property
    def r(self):
        return int(self.hex[1:3], 16)

    @property
    def g(self):
        return int(self.hex[3:5], 16)

    @property
    def b(self):
        return int(self.hex[5:7], 16)


red = Colour1("#ff0000")
# print(red.r)
# print(red.g)
# print(red.b)


class ColourComponent:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __get__(self, obj, _):
        return int(obj.hex[self.start: self.end], 16)


class Colour2:
    r = ColourComponent(1, 3)
    g = ColourComponent(3, 5)
    b = ColourComponent(5, 7)

    def __init__(self, hex):
        self.hex = hex


# red = Colour2('#ff0000')
# print(red.r)
# print(red.g, red.b)


def dijkstra(graph, start: str, end: str):
    heap: list = [(0, start, [])]
    visited = set()

    while heap:
        (cost, node, path) = heapq.heappop(heap)
        if node not in visited:
            visited.add(node)
            path = path + [node]

            if node == end:
                return path

            for neighbor, c in graph[node].items():
                heapq.heappush(heap, (cost + c, neighbor, path))

    return None


# Example usage:
graph: dict[str, dict[str, int]] = {
    "A": {"B": 1, "C": 4},
    "B": {"A": 1, "C": 2, "D": 5},
    "C": {"A": 4, "B": 2, "D": 1},
    "D": {"B": 5, "C": 1},
}

# print(dijkstra(graph, 'A', 'D'))


def longest_common_substring(str1, str2):
    m = len(str1)
    n = len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    longest_substring = ""

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > len(longest_substring):
                    longest_substring = str1[i - dp[i][j]: i]
            else:
                dp[i][j] = 0

    return longest_substring


# Example usage:
# print(longest_common_substring('abcdef', 'defghi'))  # => def


def permutations(numbers: list[int]):
    return list(itertools.permutations(numbers))


# Example usage:
# print(permutations([1, 2, 3]))


# Reverse linked-list


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def reverse(self):
        previous = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()


# Example usage:
linked_list = LinkedList()
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)

# linked_list.print_list()
linked_list.reverse()
# linked_list.print_list()


# Binary search for given sorted array of integers.


def binary_search(arr: list[int], target: int):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Example usage:

# print(binary_search([1, 2, 3, 4, 5], 3))  # => 2
# print(binary_search([1, 2, 3, 4, 5], 6))  # => -1


def quicksort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr

    pivot: int = arr[len(arr) // 2]
    left: list[int] = [x for x in arr if x < pivot]
    middle: list[int] = [x for x in arr if x == pivot]
    right: list[int] = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)


# Example usage:
arr: list[int] = [3, 1, 4, 2, 5]
# print(quicksort(arr))  # => [1, 2, 3, 4, 5]


# BFS algorithm to traverse a given tree.


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def bfs(root: Node):
    if root is None:
        return

    queue = [root]
    while len(queue) > 0:
        node = queue.pop(0)
        print(node.data, end=" ")
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)


# Example usage:

root: Node = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(bfs(root))  # 1, 2, 3, 4, 5


# Flatten a nested list
nested_list: list[list[int]] = [
    [1, 2, 3],
    [4, 5],
    [
        6,
        7,
        8,
        9,
    ],
]
flatten_list: list[int] = [item for sublist in nested_list for item in sublist]
print(flatten_list)


def flatten(lst: list) -> list[int]:
    flat_list: list[int] = []

    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)

    return flat_list


my_list = [1, [2, 3], [4, 5]]


def is_prime(num: int) -> bool:
    if num < 2:
        return False

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False

    return True


print(is_prime(7))  # True
print(is_prime(12))  # False


date_str = "2023-05-12"
date_obj = datetime.strptime(date_str, "%Y-%m-%d")
print(date_obj)


def is_palindrome(s: str) -> bool:
    return s == s[::-1]


print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))  # False


lst: list[int] = [i for i in range(1, 6)]
reversed_list = lst[::-1]


s = "Hello, world!"

if "world" in s:
    print("Substring found!")
else:
    print("Substring not found!")


a = ["banana", "apple", "cherry"]
a.sort()
print(a)


# Iterate over a dict

d: dict[str, int] = {"a": 1, "b": 2, "c": 3}

for key, value in d.items():
    print(key, value)


filename = "file.txt"

if os.path.exists(filename):
    print("File exists!")
else:
    print("File does not exist.")


# Map function
original_list: list[int] = [1, 2, 3, 4, 5]
new_list: list[int] = list(map(lambda x: x + 1, original_list))
print(new_list)

squared_list: list[int] = [x**2 for x in original_list]
print(squared_list)

even_number: list[int] = list(filter(lambda x: x % 2 == 0, original_list))
print(even_number)


product = reduce(lambda x, y: x * y, original_list)
print(product)


# Decorators

P = ParamSpec('P')  # Captuers the parameters of the decorated function
T = TypeVar('T')  # Captuers the return type of the decorated function


def timer_decorator(func: Callable[P, T]) -> Callable[P, T]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        print(f"Execution time: {end_time - start_time} seconds")

        return result

    return wrapper


@timer_decorator
def my_funciton():
    time.sleep(1)


# my_funciton()


import unittest


class MyTest(unittest.TestCase):
    def setUp(self):
        # Set up any shared state here
        self.foo = 42

    @override
    def tearDown(self) -> None:
        # Clean up any resources here
        del self.foo

    def test_something(self):
        self.assertEqual(self.foo, 42)


class MyTest1(unittest.TestCase):
    def test_almost_equal(self):
        self.assertAlmostEqual(0.1 + 0.2, 0.3, places=7)


import os
from unittest.mock import patch


def my_function1():
    with open('myfile.txt', 'w') as f:
        f.write('Hello, world!')
    return os.path.isfile('myfile.txt')


def test_my_function(mock_open):
    mock_file = mock_open.return_value.__enter__.return_value
    assert my_function1() is True
    mock_file.write.assert_called_once_with('Hello, world!')

    with patch('builtins.open', create=True) as mock_open:
        test_my_function(mock_open)


import requests
from unittest.mock import patch

def my_function2():
    response = requests.get('https://api.example.com')
    return response.json()


def test_my_function2(mock_get):
    mock_get.return_value.json.return_value = {'key': 'value'}
    assert my_function2() == {'key': 'value'}


with patch('requests.get') as mock_get:
    test_my_function2(mock_get)


def test_exception_raised():
    with self.assertRaises(MyException):
        my_function_that_raises_exception()



from unittest.mock import patch


class MyClass:
    @classmethod
    def my_class_method(cls):
        return 'Original class method'


def my_test(mock_class_method):
    with patch.object( MyClass, 'my_class_method', mock_class_method):
        assert MyClass.my_class_method() == 'Mocked class method'


def test_mock_class_method():
    my_test(lambda: 'Mocked class method')


# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base


# Base = declarative_base()


# class User(Base):
#     __tablename__ = 'users'
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
    email = Column(String)


# engine = create_engine('postgresql://your_username:your_password@localhost/your_database')

# Base.metadata.create_all(engine)


import os


password = os.environ.get('MY_APP_PASSWORD')


## Multiprocesisng

import multiprocessing


def my_function3():
    # do something
    ...


my_process = multiprocessing.Process(target=my_function3)
my_process.start()


import threading


def my_function4():
    # do something
    ...


my_thread = threading.Thread(target=my_function4)
my_thread.start()


import asyncio


async def my_coroutine():
    # do something
    ...


asyncio.run(my_coroutine())


import threading
import queue


my_queue = queue.Queue()

def producer():
    while True:
        # add items to the queue
        my_queue.put(item)


def consumer():
    while True:
        # remove items from the queue
        item = my_queue.get()



def parallel_map(func: Callable[P, T], data: list[str], num_processes: int):
    chunk_size: int = len(data) // num_processes
    chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]

    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.map(func, chunks)

    return results



### Clean Architecture Example
# app/
#     - domain/
#         - models.py
#         - repositories.py
#         - services.py
#     - application/
#         - __init__.py
#         - serializers.py
#         - use_cases.py
#         - validators.py
#     - infrastructure/
#         - __init__.py
#         - database.py
#         - repositories.py
#         - serializers.py
#     - interfaces/
#         - __init__.py
#         - api.py
#         - web.py
#     - main.py




## Control execution rate of code
import time
import functools


def reduce_execution_rate(_function=None, *, num_seconds=2):
    def decorator_exec_rate_reduction(function):
        @functools.wraps(function)
        def wrapper_rate_reduction(*args, **kwargs):
            time.sleep(num_seconds)
            return function(*args, **kwargs)
        return wrapper_rate_reduction

    if _function is None:
        return decorator_exec_rate_reduction
    else:
        return decorator_exec_rate_reduction(_function)


@reduce_execution_rate(num_seconds=3)
def clock_to_zero(start_integer):
    if start_integer < 1:
        print('Shoot!')
    else:
        print(start_integer)
        clock_to_zero(start_integer - 1)


clock_to_zero(5)


import functools


# def func_trace(method):
#     @functools.wraps(method):
#     def wrapper(*args, **kwargs):
#         logger


class LoadFile:
    def __init__(self, filename: str):
        self.filename = filename

    def __enter__(self):
        self.file_to_read = open(self.filename, 'w')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.filename
            self.filename.close()


with LoadFile('name') as f:
    f.write('some random data')


class DemoProcess:
    def __init__(self, argument):
        self.data = argument

    def __iter__(self):
        return self

    def __next__(self):
        return self.value

    # For compatibility with Python 2
    def next(self):
        return self.__next__()


def even_numbers():
    for index in range(0, 20):
        if index % 2 == 0:
            yield index


def cumulative(sequence):
    sum_till_now = 0
    for index in sequence:
        sum_till_now += index
        yield sum_till_now


class GetDoubles:
    def __init__(self, integers):
        self.integers = iter(integers)

    def __next__(self):
        return next(self.integers) * 2

    def __iter__(self):
        return self


# Alternative implementation based on functions.
def get_doubles(integers):
    for index in integers:
        yield 2*index

def get_doublse(integers):
    return (2*index for index in integers)

## Lazy summation

# The Regular Way
billable_hours = 0
for employee in all_employees:
    if employee.on_payroll():
        billable_hours += employee.time_spent


# The Pythonic Way
all_times_spent = (
    employee.time_spent
    for employee in employees
    if employee.on_payroll()
)

billable_hours = sum(all_times_spent)

## Lazy breaking out of loops

# The Regular Way
for index, content in enumerate(file_reference):
    if i >= 500:
        break
    print(content)


# The Pythonic Way
from itertools import islice

lines_iterator = islice(file_reference, 150)

for line_content in lines_iterator:
    print(line_content)


## Creating your own iteration helpers
# The Regular Way
time_diff = []
prev_time = all_call_times[0]
for curr_time in all_chill_times[1:]:
    time_diff.append(curr_time - prev_time)
    prev_time = curr_time



def itemize(iterable):
    '''Yield (prev_time, curr_time) for every iterable item.'''
    iterator = iter(iterable)
    prev_time = next(iterator)

    for curr_time in iterator:
        yield prev_time, curr_time
        prev_time = curr_time


time_diff = []
for prev_time, curr_time in itemize(all_call_times):
    time_diff.append(curr_time - prev_time)


time_diff = [
    (curr_time - prev_time)
    for prev_time, curr_time in
    itemize(all_call_times)
]


from itertools import islice


employees = islice(filter(lambda e: e.age > 40, employees), 10)
hours = EmployeeStats(employees).get_total_time()


new_emps = [
    'D Hardman', 'H Spector',
    'J Pearson', 'L Litt',
    'S Cahill', 'A Hall'
]

grouped_emps = {}

key_with_names = lambda n: n.split()[-1][0]
new_emps_sorted = sorted(new_emps, key=key_with_names)

for initial, grp_names in itertools.groupby(new_emps_sorted, key=key_with_names):
    grouped_emps[initial] = list(grp_names)

grouped_emps


def coin_change(set_of_coins, length):
    change_possible_for = set()
    for coin_subset in itertools.combinations(set_of_coins, length):
        change_possible_for.add(sum(coin_subset))
    return sorted(change_possible_for)


def median(*args):
    ...


def get_all_stats(emp_times):
    min_times, max_times, avg_times = itertools.tee(emp_times, 3)
    return (
        min(min_times),
        max(max_times),
        median(avg_times)
    )


def nested_search(elem_list, search_val):
    location = None
    for x, elem_row in enumerate(elem_list):
        for y, elem_cell in enumerate(elem_row):
            if elem_cell == search_val:
                location = (x, y)
                break

        if location is not None:
            break

    if location is None:
        raise ValueError(f'{search_val} not found')

    logger.info(f'Search successful {search_val!r}- found at {location}')

    return location


# The Pythonic Way
def _search_matrix(matrix):
    for x, elem_row in enumerate(matrix):
        for y, elem_cell in enumerate(elem_row):
            yield (x, y), elem_cell


def search(matrix, search_val):
    try:
        location = next(
            location for (location, elem_cell) in _search_matrix(matrix)
            if elem_cell == search_val
        )

    except StopIteration:
        raise ValueError(f'{search_val} not found')

    logger.info(f"Search successful - {search_val!r} found at {location}")

    return location



async def summation(begin, end, wait):
    result = 0
    for i in range(begin, end):
        result += i

    # Wait for assigned seconds
    await asyncio.sleep(wait)
    print(f"Summation from {begin} to {end} is {result}")

async def async_main():
    task_one = loop.create_task(summation(5, 500_000, 3))
    task_two = loop.create_task(summation(2, 500_000, 2))
    task_three = loop.create_task(summation(10, 500_000, 1))

    # Run teh tasks asynchronously
    await asyncio.wait([task_one, task_two, task_three])


if __name__ == '__main__':
    # Declare event loop
    loop = asyncio.get_event_loop()

    # Run the code until completing all task
    loop.run_until_complete(async_main())
    loop.close()


def fibonacci(n):
    if n <= 2:
        return 1
    if not hasattr(fibonacci, 'cache'):
        fibonacci.cache = {}
    if n not in fibonacci.cache:
        fibonacci.cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

    return fibonacci.cache[n]


def cached(f):
    cache = {}
    def worker(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return worker


@cached
def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci(n):
    series = [1, 1]
    while len(series) < n:
        series.append(series[-1] + series[-2])

    return series[-1]


def fibonacci(n):
    previous = 1
    current = 1
    for i in range(n - 2):
        next = current + previous
        previous, current = current, next

    return current



def max_profit(daily_price):
    def get_best_profit(day, have_stock):
        '''
        Returns the best profit that can be obtained by the end of the day.
        At the end of the day:
        * if have_stock is True, the trader must own the stock:
        * if have_stock is False, the trader must not own the stock;
        '''
        # TODO ...
        ...
    # Final state: end of last day, no shares owned.
    last_day = len(daily_price) - 1
    no_stock = False
    return get_best_profit(last_day, no_stock)


@lru_cache(maxsize=None)
def get_best_profit(day, have_stock):
    ...
