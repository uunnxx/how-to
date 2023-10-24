from math import sqrt
import _thread as thread


def is_prime(x: int):
    if x < 2:
        print(f'{x} is not a prime number.')
    elif x == 2:
        print(f'{x} is a prime number.')
    elif x % 2 == 0:
        print(f'{x} is not a prime number.')
    else:
        limit = int(sqrt(x)) + 1
        for i in range(3, limit, 2):
            if x % i == 0:
                print(f'{x} is not a prime number.')

        print(f'{x} is a prime number.')


inputs = [2, 193, 323, 1327, 433785907]

for x in inputs:
    thread.start_new_thread(is_prime, (x, ))
