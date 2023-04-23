class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)





emp_1 = Employee('Corney', 'Schafer', 50_000)
emp_2 = Employee('Test', 'User', 60_000)


# print(emp_1.__dict__)
print("------------------------------------------------------------")
# print(Employee.__dict__)
print(Employee.num_of_emps) # 2

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
