from birdseye import eye


@eye
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)


factorial(10)
print(factorial(5))
