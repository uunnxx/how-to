# classes and objects
# functions, methods, and properties
# polymorphism and special dunder methods
# single inheritance
# descriptors
# enumerations
# exception

def br():
    print(f"\n{'-' * 80}\n")


br()


class Person:
    pass


p = Person()


print(f"{type(Person)=}")
print(f"{type(type)=}")
print(f"{Person.__name__=}")
print(f"{p=}")
print(f"{p.__class__=}")
print(f"{type(p) is p.__class__=}")

print(f"{isinstance(p, Person)=}")
print(f"{isinstance('hello', str)=}")

