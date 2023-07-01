class SomeClass:
    pass


some_object = SomeClass()
print(type(some_object))


import inspect

inspect.isclass(SomeClass)
inspect.isclass(some_object)
inspect.isclass(type(some_object))

