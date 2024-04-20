class ImmutablePoint:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __eq__(self, other):
        if not isinstance(other, ImmutablePoint):
            return False

        return self._x == other._x and self._y == other._y

    def __hash__(self):
        return hash((self._x, self._y))

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y



ip = ImmutablePoint(10, 20)

print(ip.x, ip.y)

# ip.x = 'changed'
ip2 = ImmutablePoint(10, 20)

ip == ip2


d = {ip: 'hello'}

print(d[ip])
print(d[ip2])


import collections


class HashableList(collections.UserList):
    def __hash__(self):
        return hash(tuple(self))


h = HashableList([1, 2, 3])
d = {h: 'hello'}
print(d)


h2 = HashableList([1, 2, 3])

print(d[h2])

h[2] = 100

print(d[h])
