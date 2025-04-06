## Lowercase & uppercase

#include <stdio.h>

# int main() {
#     // Convert to lowercase
#     printf("'a' => '%c'\n", ('a' | ' '));
#     printf("'A' => '%c'\n", ('A' | ' '));
#
#     // Convert to uppercase
#     printf("'a' => '%c'\n", ('a' & '_'));
#     printf("'A' => '%c'\n", ('a' & '_'));
#
#     return 0;
# }


def lowercase(string: str) -> str:
    result: list[str] = []

    for char in string:
        result.append(chr(ord(char) | ord(' ')))

    return ''.join(result)


def uppercase(string: str) -> str:
    result: list[str] = []
    for char in string:
        if char != ' ':
            result.append(chr(ord(char) & ord('_')))
        else:
            result.append(char)

    return ''.join(result)



print(lowercase('Some Text'))
print(uppercase('Some Text'))


# right shift (>>): division by 2
print(40 >> 1)  # 4 / (2**1)
print(40 >> 2)  # 4 / (2**2)
print(40 >> 3)  # 4 / (2**3)


# left shift (>>): multiplication by 2
print(40 << 1)  # 4 * (2**1)
print(40 << 2)  # 4 * (2**2)
print(40 << 3)  # 4 * (2**3)


# and (&) operator to check even or odd number
def is_odd(num: int) -> bool:
    # return bool(num & 1)
    # return not not num & 1
    return num & 1 == 1


def is_even(num: int) -> bool:
    # return not num & 1
    # return not bool(num & 1)
    return num & 1 == 0

print()

print(is_odd(4))
print(is_odd(5))

print(is_even(4))
print(is_even(5))
