from dataclasses import dataclass
from typing import Callable, TypeVar, Iterable


Phone = str


@dataclass
class User:
    user_id: int
    phone: Phone


def get_user_phone(user: User) -> Phone:
    return user.phone


def my_sym(a: int, b: int) -> int:
    return a + b


def process_operation(operation: Callable[[int, int], int], a: int, b: int) -> int:
    return operation(a, b)


def find_book_in_library(*args):
    pass


def get_user_by_username(*args):
    pass


book: str = 'name of the book'  # too much
book: str = find_book_in_library('name of the book')  # it's ok, because of return type


user: User = get_user_by_username('Username')


class SomeClass:
    def __init__(self):
        self._some_dict: dict[str, int] = {}

    def some_method(self):
        self._some_dict['some_key'] = 123  # ok
        self._some_dict[123] = 'some_key'  # type error


T = TypeVar('T')

def first(iterable: Iterable[T]) -> T | None:
    for element in iterable:
        return element


INT_FLOAT = TypeVar('Int or Float')
def adder(a: INT_FLOAT, b: INT_FLOAT) -> INT_FLOAT:
    return a + b


print(adder(1, 2))
print(adder(1.5, 1.5))


print(first(['one', 'two']))  # one
print(first((100, 200)))  # 100
