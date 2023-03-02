def fizzbuzz(n):
    lst = []
    fizz = None
    buzz = None

    for i in range(1, n + 1):
        fizz = i % 3 == 0
        buzz = i % 5 == 0

        if [fizz, buzz] == [True, True]:
            lst.append("FizzBuzz")
        elif [fizz, buzz] == [True, False]:
            lst.append("Fizz")
        elif [fizz, buzz] == [False, True]:
            lst.append("Buzz")
        else:
            lst.append(i)

    return lst


# print(fizzbuzz(100))


# Itertools cycle()
###############################################################################
# RUBY
#
# def fizzbuzz
#   fizzy = [nil, nil, :Fizz].cycle
#   buzzy = [nil, nil, nil, nil, :Buzz].cycle
#
#   (1..100).map do |n|
#      "#{fizzy.next}#{buzzy.next}"[/.+/] || n
#   end
# end

from itertools import cycle
import re


def fizzbuzz_cycle(n):
    fizzy = cycle(['', '', 'Fizz'])
    buzzy = cycle(['', '', '', '', 'Buzz'])
    for i in range(1, n + 1):
        fizzbuzz = next(fizzy) + next(buzzy)
        match = re.search(r'.+', fizzbuzz)
        print(match[0]) if match else print(i)

        # if m:
        #     print(m[0])
        # else: i

        # if fizz and buzz:
        #     print(fizz + buzz)
        # elif fizz:
        #     print(fizz)
        # elif buzz:
        #     print(buzz)
        # else:
        #     print(i)


# fizzbuzz_cycle(100)


import itertools

def fizz_buzz(n):
    fizzes = itertools.cycle([''] * 2 + ['Fizz'])
    buzzes = itertools.cycle([''] * 4 + ['Buzz'])

    fizzes_buzzes = (fizz + buzz for fizz, buzz in zip(fizzes, buzzes))
    result  = (word or n for word, n in zip(fizzes_buzzes, itertools.count(1)))

    for i in itertools.islice(result, 100):
        print(i)


# Lambda
# print(*map(lambda i: 'Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or i, range(1, 101)), sep='\n')




# String concatenation
# for num in range(1, 101):
#     string = ''
#     if num % 3 == 0:
#         string += 'Fizz'
#     if num % 5 == 0:
#         string += 'Buzz'
#     if num % 5 != 0 and num % 3 != 0:
#         string += str(num)
#     print(string)


# Hashtable

def fizz_buzz_game(n):
    output = []
    # Initialize a dictionary to store the mapping of numbers to strings
    fizz_buzz = {3: 'Fizz', 5: 'Buzz'}

    for i in range(1, n+1):
        s = ''
        # Check if the current number is divisible by any of the
        # keys in the dictionary
        for key in fizz_buzz:
            if i % key == 0:
                s += fizz_buzz[key]

        # If the number is not divisible by any oof the keys,
        # store the number itself
        if s == '':
            s = str(i)
        output.append(s)
    return output


# print(fizz_buzz_game(100))


