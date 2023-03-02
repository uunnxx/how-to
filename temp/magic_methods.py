class Url():
    def __init__(self, url):
        self._url = url

    def __div__(self, x):
        return self.__class__(f"{self._url}/{x}")

    def __str__(self):
        return self._url


# print(Url('') / 'main')

# print(dir(object))

# class Pipe(object): explicit inheritance from object for python2

class Pipe():
    def __init__(self, fn=lambda x: x):
        self._fn = fn

    def __or__(self, fn):
        return self.__class__(lambda x: fn(self._fn(x)))

    def __call__(self, arg):
        return self._fn(arg)


f = Pipe() | abs | str | len
print(f(1000000000000000000))

print((Pipe() | abs | str | len)(10))
