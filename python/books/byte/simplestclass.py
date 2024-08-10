class Person:
    def __init__(self, name: str):
        self.name = name

    def say_hi(self):
        print(f'Hi there!\nMy name is {self.name}')


# p = Person('Swaroop')
# p.say_hi()


class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        print(f"(Initializing {self.name})")

        Robot.population += 1


    def __del__(self):
        print(f"Destroying {self.name}")

        Robot.population -= 1

        if Robot.population == 0:
            print(f"{self.name} was last Robot")
        else:
            print(f"{Robot.population} left")

    def say_hi(self):
        print(f"Hello!\nMy owner calls me {self.name}")

    # @staticmethod
    def how_many():
        print(f"We have {Robot.population} robots.")

    how_many = staticmethod(how_many)


# droid1 = Robot('R2-D2')
# droid1.say_hi()

# Robot.how_many()

# droid2 = Robot('C-3PO')
# droid2.say_hi()

# Robot.how_many()



from abc import ABCMeta, abstractmethod


class SchoolMember(metaclass=ABCMeta):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"(Created SchoolMember: {self.name})")


    @abstractmethod
    def tell(self):
        print(f"Name: {self.name} Age: {self.age}", end=" ")


class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print(f"(Created Teacher: {self.name})")

    def tell(self):
        SchoolMember.tell(self)
        print(f"Salary: {self.salary}")


class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print(f"(Created Student: {self.name})")

    def tell(self):
        SchoolMember.tell(self)
        print(f"Score: '{self.marks}'")


# t = Teacher('Mrs. Schrividya', 40, 30_000)
# s = Student('Swaroop', 25, 75)


# print()


# members = [t, s]
# for member in members:
#     member.tell()


class ShortInputException(Exception):
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast


try:
    text = input('Type something: ')
    length = len(text)
    if length < 3:
        raise ShortInputException(length, 3)
    # do something
except EOFError:
    print('End of file')
except ShortInputException as ex:
    print(f'Short input length: expected at least {ex.length}')
else:
    print('Everything is ok! No Exception!')
