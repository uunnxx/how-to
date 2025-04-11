from typing import Optional
from fastAPI import FastAPI, Query
import requests


requests.get


app = FastAPI()
app.ge


class Monster:
    # attributes
    health = 90
    energy = 40

    # methods
    def attack(self, amount):
        print('The monster has attacked!')
        print(f'{amount} damage was dealt')
        monster.energy -= 20
        print(monster.energy)

    def move(self, speed):
        print("The monster has moved")
        print(f"It has a speed of {speed}")

#
# monster = Monster()
# monster.__ne__
#
# # Monster.attack(monster)
# # monster.attack(40)
# monster.move(20)
#


import inspect


class MonkeyPatch:
    def __init__(self, n):
        self.n = n

    def add(self, other):
        return (self.n + other)


obj = MonkeyPatch(10)
obj.add(20)
print(inspect.getmembers(obj, predicate=inspect.ismethod))

def divide(self, n2):
    return (self.n - self.n2)

MonkeyPatch.divide = divide


print('-' * 80)

print(inspect.getmembers(obj, predicate=inspect.ismethod))
