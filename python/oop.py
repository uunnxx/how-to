# Object-oriented programming (OOP) is a programming paradigm that uses objects to represent and manipulate data. Python is a popular language for OOP, with support for classes, inheritance, encapsulation, and polymorphism. Here are some advanced code examples of OOP in Python:

# Example 1: Inheritance
# Inheritance allows us to create new classes that are modified versions of existing classes. In Python, we can use the super() function to call the parent class's methods. Here's an example:


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError('Subclass must implement this abstract method')

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return 'Woof!'

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return 'Meow!'


dog = Dog('Fido')

print(dog.name)
print(dog.speak())

cat = Cat('Whiskers')
print(cat.name)
print(cat.speak())


# In this example, we define an Animal class with an __init__ method that initializes the name attribute, and a speak method that raises a NotImplementedError to indicate that it is an abstract method and must be implemented by any subclass that inherits from it.

# We then define two subclasses of Animal: Dog and Cat. Each subclass overrides the speak method with its own implementation.

# Finally, we create instances of the Dog and Cat classes, and call their name and speak methods.

# Example 2: Encapsulation
# Encapsulation allows us to hide implementation details from the outside world and restrict access to certain attributes or methods. In Python, we can use the underscore prefix to indicate private attributes or methods.

# Here's an example:


class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
        else:
            raise ValueError('Insufficient balance')

    def get_balance(self):
        return self._balance


account = BankAccount(100)
print(account.get_balance())
account.deposit(50)
print(account.get_balance())
account.withdraw(75)
print(account.get_balance())


# In this example, we define a BankAccount class with an __init__ method that initializes the balance attribute, and three methods: deposit, withdraw, and get_balance.

# We use the underscore prefix to indicate that balance is a private attribute, which should not be accessed or modified directly by outside code.

# The deposit method adds the specified amount to the balance.

# The withdraw method subtracts the specified amount from the balance, but raises a ValueError if the balance is insufficient.

# The get_balance method returns the current balance.

# Finally, we create an instance of the BankAccount class, and call its methods to deposit, withdraw, and get the balance.


# Example 3: Polymorphism
# Polymorphism allows us to use objects of different classes in the same way, as long as they have the same interface (i.e. methods with the same name and parameters). In Python, we can use the @abstractmethod decorator to define abstract methods that must be implemented by any subclass that inherits from it. Here's an example


class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


shapes = [Rectangle(5, 10), Circle(7)]
for shape in shapes:
    print(shape.area())


# In this example, we define a Shape class with an area method that does nothing, effectively making it an abstract method.

# We then define two subclasses of Shape: Rectangle and Circle. Each subclass overrides the area method with its own implementation.

# Finally, we create a list of Shape objects, containing one Rectangle and one Circle, and call the area method on each object. The area method is polymorphic, in that it behaves differently for Rectangle and Circle, but we can call it on both types of objects in the same way.







###############################################################################




# Object-Oriented Programming (OOP) is a programming paradigm that organizes code into objects that interact with each other. Python is an object-oriented language that fully supports OOP concepts, such as:

# 1. Encapsulation: This is the practice of hiding the internal implementation details of an object from the outside world. In Python, this is achieved through the use of public, private, and protected access modifiers.

# 2. Inheritance: This is the process of defining a new class based on an existing class. The new class inherits all the attributes and methods of the existing class and can also add its own attributes and methods.

# 3. Polymorphism: This is the ability of different objects to respond to the same message or method call in different ways. Polymorphism in Python is achieved through method overriding and method overloading.

# 4. Abstraction: This is the process of hiding complex implementation details and exposing only the necessary information to the outside world. In Python, this can be achieved through the use of abstract classes and interfaces.

# Here's an example that demonstrates some of these concepts:


# Example class hierarchy

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Example usage

animals = [Dog("Rex"), Cat("Fluffy")]

for animal in animals:
    print(animal.name + " says " + animal.speak())


# In this example, we have an Animal class with an abstract speak method. We then define two subclasses, Dog and Cat, that override the speak method with their own implementations.

# We then create a list of Animal objects, containing one Dog and one Cat, and call the speak method on each object. The speak method is polymorphic, in that it behaves differently for Dog and Cat, but we can call it on both types of objects in the same way.

# This example also demonstrates inheritance, where the Dog and Cat classes inherit from the Animal class, and encapsulation, where the name attribute of each animal object is encapsulated within the object and not directly accessible from outside the object.





# Abstraction is the process of hiding the implementation details of a class or function and exposing only the necessary information to the outside world. In Python, we can achieve abstraction through the use of abstract classes and interfaces.

# Here's an example that demonstrates abstraction in Python using abstract classes:



from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

shapes = [Rectangle(5, 10), Circle(7)]
for shape in shapes:
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())



# In this example, we define an abstract Shape class with two abstract methods, area and perimeter. We then define two subclasses of Shape, Rectangle and Circle, that implement the area and perimeter methods in their own way.

# Since Shape is an abstract class, we cannot create instances of it directly. Instead, we create instances of its subclasses Rectangle and Circle, and call their area and perimeter methods.

# This example demonstrates abstraction by hiding the implementation details of the Shape class and only exposing the necessary methods to the outside world. The users of the Shape class do not need to know how the area and perimeter methods are implemented; they only need to know what methods are available and how to use them.
