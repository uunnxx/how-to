import inspect


class SomeClass:
    pass


some_object = SomeClass()
print(type(some_object))


inspect.isclass(SomeClass)
inspect.isclass(some_object)
inspect.isclass(type(some_object))
