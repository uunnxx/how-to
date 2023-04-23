class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@company.com'

    # without self
    # @classmethod
    # def fullname(cls):
    #     return '{} {}'.format(first, lat)

    def fullname(self):
        return f'{self.first} {self.last}'

emp_1 = Employee('Corney', 'Schafer', 50_000)
# def __init__ (self: emp_1, first: Corney, last: Schafer, pay: 50_000)

emp_2 = Employee('Test', 'User', 60_000)
# def __init__ (self: emp_2, first: Test, last: User, pay: 60_000)


# print object id
# print(emp_1)
# print(emp_2)

# print(emp_1.first)
# print(emp_2.first)

# print(emp_1.fullname())

# when we call it from class we need to add instance as an argument

print(emp_1.fullname())
# same as:
print(Employee.fullname(emp_1))


# emp_1.fullname()
# it'll be converted to in the background:
# Employee.fullname(emp_1)
