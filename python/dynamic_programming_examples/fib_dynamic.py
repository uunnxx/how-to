import time
import matplotlib.pyplot as plt


calculated = {}

def fib(n: int):
    if n == 0:  # base case 1
        return 0
    if n == 1:  # base case 2
        return 1
    elif n in calculated:
        return calculated[n]
    else:
        calculated[n] = fib(n-1) + fib(n-2)
        return calculated[n]


show_number = False
numbers = 20
