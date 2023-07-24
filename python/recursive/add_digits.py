def add_digits(n: int) -> int:
    if n < 10:
        return n
    else:
        return add_digits(n // 10) + (n % 10)


print(add_digits(5))
print(add_digits(15))
print(add_digits(16))
print(add_digits(27))
print(add_digits(30))
print(add_digits(33))
