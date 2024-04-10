import random
import pdb


print('Guess a number between 1 and 10')
number: int = random.randint(1, 10)

pdb.set_trace()

guess: int = int(input())


if guess == number:
    print(f'Correct - the number was {number}')
else:
    print(f'Sorry, the number waas {number}, not {guess}')
