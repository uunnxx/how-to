class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

# e1 = Employee("Vera", "Schmidt", 2000)
# e2 = Employee("Chuck", "Murphy", 1800)
# e3 = Employee("Dave", "Dreissing", 1900)
#
# print(e1.first_name, e1.last_name, e1.salary)
# print(e2.first_name, e2.last_name, e2.salary)
# print(e3.first_name, e3.last_name, e3.salary)


employee = [
    Employee("Vera", "Schmidt", 2000),
    Employee("Chuck", "Murphy", 1800),
    Employee("Dave", "Dreissing", 1900)
]

for e in employee:
    print(e.first_name, e.last_name, e.salary)
