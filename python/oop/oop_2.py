import subprocess


x: list = [1, 2]
y: list = [3, 4]


class Base:
    pass


class Purse(Base):
    def __init__(self, name: str):
        self.name = name

    def show(self):
        return f'{self.name}'



purse: Base = Purse('Python')

# print(type(purse))

# print(purse.show())


class Action:
    def __init__(self, actions):
        self.actions = actions

    def do_it(self):
        for action in self.actions:
            subprocess.run(action)


hellos = Action([
    ['echo', 'Hello world'],
    ['echo', 'Bonjour le monde']
])


# hellos.do_it()


class Action2:
    def __init__(self, actions):
        self.actions = actions

    def __call__(self):
        for action in self.actions:
            subprocess.run(action)


hellos2 = Action2([
    ['echo', 'Hello world'],
    ['echo', 'Bonjour le monde']
])


# hellos2()




# Parenthesis invoke
# - Parenthesis cause an object to be called
# - Everytihng is an object

# >> print      # <bulit-in function print>
# >> print()    #





# Object creation is invocation
# - Classes are objects
# - Instantiating an object from a class uses parenthesis on the class
#     - Invoking the class!
# - All classes inherit from the `type` metaclass
# - The `type` metaclass has a `__call__()` method
# - The `__call__()` method invokes `__new__()` and `__init__()`
# - Default methods for `__new__()` and `__init__()` are provided in the class hierarchy
# - `__new__()` is responsible for object creation
# - `__init__()` is responsible for initialization


def new(cls):
    obj = object.__new__(cls)
    obj.description = 'Amuse your mouth'
    return obj

AmuseBouche = type('AmuseBouche', (), {
    '__new__': new,
})

ceviche = AmuseBouche()
# print(ceviche.description)


# - The `__new__()` method is invoked to create the object.
# - What if you want to do something when a class is created?
# - Cannot override `type.__new__`
# - Class inheritance syntax allows for a `metaclass` argument
#     - Create a special class that inherits from `type`
#     - Override `__new__()` on that class
#     - Use teh special metaclass when edclaring another class

class CounterMeta(type):
    count = 0
    def __new__(cls, name, bases, dct):
        klass = super().__new__(cls, name, bases, dct)
        cls.count += 1
        return klass


class Pie(metaclass=CounterMeta):
    pass


apple = Pie()
raspberry = Pie()

# apple.count # attribute error
print(apple.__class__.count)
print(raspberry.__class__.count)


class Cake(metaclass=CounterMeta):
    pass


chocolate = Cake()
vanilla = Cake()
print(vanilla.__class__.count)  # 2 (2 uses of CounterMeta)


class Friend:
    def __init__(self, friends):
        self.friends = friends

    def is_friend_of(self, name):
        return name in self.friends

    def __call__(self, *args):
        head, *tail = args
        print(head, tail)
        # self.head(tail)


# i.e.
# def is_my_friend(name):
#     return name in friend_names
#
# def buddy(method_name, *args):
#     if method_name == 'is_friend_of':
#         return is_my_friend(*args)


buddy = Friend(['alan', 'alonzo'])
print(buddy.is_friend_of('guy'))
print(buddy.is_friend_of('alan'))

print(Friend.__dict__)


# buddy.is_friend_of('guy')
# buddy.send(:is_friend_of, 'guy')
buddy('is_friend_of', 'guy')


# class True
#     if True: a if False: b
#         ^ a value
#
# class False
#     if True: a if False: b
#         ^ b value
#
# As, TRUE  := \x.\y.x
#     FALSE := \x.\y.y
# Lambda calculus
