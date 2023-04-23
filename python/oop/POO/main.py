import uuid
import datetime
def br():
    print(f"\n{'-' * 80}\n")


def stock_info(company, country, price, currency):
    return (
        f"Company: {company}\n"
        f"Country: {country}\n"
        f"Price: {price}"
    )


print(stock_info.__code__.co_varnames)


br()


counter = 1

def update_counter():
    global counter
    counter += 1
    print(counter)


update_counter()


br()


count = 0
dot_count = ''

def update_count():
    global count, dot_count
    count += 1
    dot_count += '.'


[update_count() for _ in range(40)]
print(count)
print(dot_count)


br()


def display_info(number_of_updates=1):
    counter = 100
    dot_counter = ''

    def update_counter():
        nonlocal counter, dot_counter
        counter += 1
        dot_counter += '.'

    [update_counter() for _ in range(number_of_updates)]

    print(counter)
    print(dot_counter)


display_info(10)


br()


# __dict__
for name in sorted(datetime.__dict__):
    print(name)


br()


class Product:
    def __init__(self, product_name, product_id, price):
        self.product_id = self.get_id()
        self.product_name = product_name
        self.price = price

    def __repr__(self):
        return f"Product(product_name='{self.product_name}', price={self.price})"

    @staticmethod
    def get_id():
        return str(uuid.uuid4().fields[-1])[:6]


product = Product('Mobile Phone', '54274', 2900)
print(product.__dict__)

br()

for name in Product.__dict__:
    print(name)


br()


def stick(*args):
    args = [arg for arg in args if isinstance(arg, str)]
    return '#'.join(args)


print(stick('sport', 'summer'))
print(stick(3, 5, 7))
print(stick(False, 'time', True, 'workout', [], 'gym'))


br()


def display_info1(company, **kwargs):
    print(f"Company name: {company}")
    if 'price' in kwargs:
        print(f"Price: ${kwargs['price']}")


display_info1(company='CD Project', price=100)


br()


def display_info2(company, **kwargs):
    print(f"Company name: {company}")
    if kwargs:
        for name in kwargs:
            print(f"{name.title()}: {kwargs[name]}")


display_info2(company='CD Project', price='100', coworkers=1550)


br()


class Vehicle:
    """This is a Vehicle class"""


print(Vehicle.__name__)

br()


class Container:
    """This is a Container class"""


print(Container.__dict__.keys())

br()
