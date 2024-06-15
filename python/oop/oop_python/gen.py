def concatenate(sources):
    for a in sources:
        for item in a:
            yield item


x = [[1, 2, 3], [4, 5, 6]]

a= concatenate(x)
print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

def concatenate2(sources):
    for items in sources:
        yield from items


b = concatenate2(x)
print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))


def countdown(n):
    while n > 0:
        yield n
        n -= 1


def countup(stop):
    n = 0
    while n < stop:
        yield n
        n += 1


def combined_gen(n):
    yield from countdown(n)
    yield from countup(n)


def recv_count():
    try:
        while True:
            n = yield
            print(n)
    except GeneratorExit:
        print('exception occure')


r = recv_count()
print(r.send(None))  # Have to send None to start this thing off

for i in range(5, 0, -1):
    r.send(i)
