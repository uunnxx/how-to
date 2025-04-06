from typing import NamedTuple
from dataclasses import dataclass


class User:
    def __init__(self, user_id: int):
        self.user_id: int = user_id
        self.preferences = {}

    def add_preference(self, item_id: int, rating: int):
        ...




class Stock(NamedTuple):
    symbol: str
    current: float
    high: float
    low: float

    @property
    def middle(self) -> float:
        return (self.high + self.low) / 2


s = Stock('AAPL', 123.52, 137.98, 53.15)
print(s.middle)



@dataclass(order=True)
class Stock2:
    symbol: str
    current: float
    high: float
    low: float


class StockOrdinary2:
    def __init__(self, name: str, current: float, high: float, low: float) -> None:
        self.name = name
        self.current = current
        self.high = high
        self.low = low


@dataclass(order=True)
class StockOrdinary:
    name: str
    current: float = 0.0
    high: float = 0.0
    low: float = 0.0


s_ord = StockOrdinary('AAPL', 123.52, 137.98, 53.15)
s_ord2 = StockOrdinary('AAPL', 123.52, 137.98, 53.15)

print(s_ord == s_ord2)


class HTMLRenderer:
    def start_paragraph(self):
        print('<p>')

    def end_paragraph(self):
        print('</p>')

    def sub_emphasis(self, match):
        return '<em>%s</em>' % match.group(1)

    def feed(self, data):
        print(data)


class Handler:
    def callback(self, prefix, name, *args):
        method = getattr(self, prefix+name, None)
        if callable(method): return method(*args)

    def start(self, name):
        self.callback('start_', name)

    def end(self, name):
        self.callback('end_', name)

    def sub(self, name):
        def substitution(match):
            result = self.callback('sub_', name, match)
            default = match.group(0)
            return result or default

        return substitution


class Meteor:
    def __init__(self):
        self.meteors: list[str] = []

    def rect(self):
        ...


class Collision(Meteor):
    starship = []
    def __init__(self):
        ...

    def rect(self):
        ...

    def _check_for_collision(self):
        '''
        Checks to see if any of the meteors have collided
        with the starship
        '''
        result = False
        for meteor in self.meteors:
            if self.starship.rect().colliderect(meteor.rect()):
                result = True
                break
            return result
