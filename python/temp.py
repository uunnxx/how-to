def count_up_to(n: int):
    i = 0
    while i <= n:
        yield i
        i += 1


counter = count_up_to(10)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
