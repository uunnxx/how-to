# Metaprogramming in Python is the ability to create code that can manipulate other code at runtime. One way to achieve this in Python is by accessing and manipulating the __dict__ attribute of a class or object. The __dict__ attribute is a dictionary that holds the attributes of an object, including its methods and properties. Here's an example of using __dict__ for metaprogramming in Python:


class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y


obj = MyClass(2, 3)

# Using __dict__ to access object attributes
print(obj.__dict__)

# Using __dict__ to add object attributes dynamically
obj.__dict__['z'] = 5
print(obj.z)

# Using __dict__ to add methods dynamically
def sub(self):
    return self.x - self.y


obj.__class__.sub = sub
print(obj.sub())

# Using __dict__ to access class attributes
print(MyClass.__dict__)

# Using __dict__ to add class attributes dynamically
MyClass.__dict__['z'] = 10
print(MyClass.z)

# Using __dict__ to add class methods dynamically
@classmethod
def multiply(cls, x, y):
    return x * y


MyClass.__dict__['multiply'] = multiply
print(MyClass.multiply(2, 3))


# In the above example, we first define a MyClass class with an __init__ method that initializes the x and y attributes of an object, and an add method that returns the sum of x and y.

# We then create an object obj of the MyClass class with x = 2 and y = 3.

# We can access the attributes of the obj object using the __dict__ attribute, which returns a dictionary containing the attributes of the object.

# We can also add attributes to the obj object dynamically by modifying its __dict__ attribute. In this example, we add a new attribute z to the obj object with the value 5.

# We can also add methods to an object dynamically by modifying its class's __dict__ attribute. In this example, we define a new function sub that subtracts y from x, and add it to the MyClass class's __dict__ attribute as a new method.

# We can access the attributes of the MyClass class using its __dict__ attribute, which returns a dictionary containing its attributes.

# We can also add attributes to the MyClass class dynamically by modifying its __dict__ attribute. In this example, we add a new class attribute z to the MyClass class with the value 10.

# We can also add class methods to a class dynamically by modifying its __dict__ attribute. In this example, we define a new function multiply that multiplies x and y, and add it to the MyClass class's __dict__ attribute as a new class method.

# The output of the above code will be:


{'x': 2, 'y': 3}
# 5
# -1

{
    '__module__': '__main__',
    '__init__': < function MyClass.__init__ at 0x7fc1221ef310 >,
    'add': < function MyClass.add at 0x7fc1221ef3a0 >,
    '__dict__': < attribute '__dict__' of...
}
