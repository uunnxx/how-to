import datetime


class User:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    def __repr__(self):
        return f"{self.name=} is a {self.occupation=}"

    def __str__(self):
        return f"{self.name} is a {self.occupation}"


u = User('John Doe', 'gardener')

print(f'{u!r}')
print(f'{u!s}')


now = datetime.datetime.now()


print()
print(f'{now:%Y-%m-%d %H:%M}')
print(f'{now:%A}')
print(f'{now:%a}')
print(f'{now:%B}')
print(f'{now:%j}')
print(f'{now:%w}')
