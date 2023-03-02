def br():
    print()
    print('-' * 80)
    print()


br()


class Person:
    # pass  # An empty block
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)


p = Person('Swaroop')

p.say_hi()


br()


class Robot:
    """Represents a robot, with a name."""

    # A cclass variable, counting teh number of robots
    population = 0

    def __init__(self, name):
        """Initializes the data."""
        self.name = name
        print(f"(Initializing {self.name})")

        # When this person is created, the robot
        # adds to the population
        Robot.population += 1

    def die(self):
        """I'm dying."""
        print(f"{self.name} is being destroyed.")

        Robot.population -= 1

        if Robot.population == 0:
            print(f"{self.name} was the last one.")
        else:
            print(
                f"------ There are still {Robot.population:d}",
                "robots working ------")

    def say_hi(self):
        """
        Greetings by the robot.
        Yeah, they can do that.
        """
        print(f"Greetings, my masters call me {self.name}.")

    @classmethod
    def how_many(cls):
        """Prints the current population."""
        print(f"We have {cls.population:d} robots.")


droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

br()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()

Robot.how_many()

br()


class SchoolMember:
    '''Represents any school member.'''

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"(Initialized SchoolMember: {self.name}).")

    def tell(self):
        '''Tell my details.'''
        print(f"Name: \"{self.name}\" Age: \"{self.age}\"", end=' ')


class Teacher(SchoolMember):
    '''Represents a teacher.'''

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print(f"(Initialized Teacher: {self.name}).")

    def tell(self):
        SchoolMember.tell(self)
        print(f"Salary: \"{self.salary:d}\"")


class Student(SchoolMember):
    '''Represents a student.'''

    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print(f"(Initialized Student: {self.name})")

    def tell(self):
        SchoolMember.tell(self)
        print(f"Marks: \"{self.marks:d}\"")


t = Teacher('Mrs. Shrividya', 40, 30_000)
s = Student('Swaroop', 25, 75)


br()


members = [t, s]
for member in members:
    member.tell()


br()





