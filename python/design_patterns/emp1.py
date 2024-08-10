

"""
"""
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def raise_salary(self, factory):
        return self.salary * factory

    def save_as_xml(self):
        pass

    def print_employee_report(self):
        pass


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def raise_salary(self, factory):
        return self.salary * factory

    def save_as_xml(self):
        with open('emp.xml', 'w') as file:
            file.write(f"<xml><name>{self.name}</name><salary>{self.salary}</salary></xml>")


class Employee:
    xml_filename = 'emp.xml'

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def raise_salary(self, factory):
        return self.salary * factory

    def save_as_xml(self):
        with open(self.xml_filename, 'w') as file:
            file.write(f"<xml><name>{self.name}</name><salary>{self.salary}</salary></xml>")


class Employee:
    xml_filename = 'emp.xml'

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def raise_salary(self, factory):
        return self.salary * factory


class Reporting:
    def print_receipt(self, receipt_text):
        pass


class CashRegisterPrinter:
    def print_receipt(self, receipt_text):
        print('Print receipt_text to CashRegisterPrinter')



