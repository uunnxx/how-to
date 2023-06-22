def is_fizzy(num: int) -> bool:
    return (num % 3 == 0)

def is_buzzy(num: int) -> bool:
    return (num % 5 == 0)

def is_fuzz_buzz(num: int) -> int:
    if is_fizzy(num) and is_buzzy(num):
        return 0
    if is_fizzy(num):
        return 1
    if is_buzzy(num):
        return 2
    return 3


def fizzbuzz(num: int):
    for i in range(1, num+1):
        match is_fuzz_buzz(i):
            case 0:
                print('FizzBuzz')
            case 1:
                print('Fizz')
            case 2:
                print('Buzz')
            case _:
                print(i)


if __name__ == '__main__':
    fizzbuzz(15)
