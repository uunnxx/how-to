class Dog:
    # name = 'Rex'
    # color = 'Orange-Black'

    def __init__(self, name, color) -> None:
        self.name = name
        self.color = color

    def bark(self):
        print(f'{self.name} is barking -- woof-woof')

    def __str__(self) -> str:
        return f'Name: {self.name}\nColor: {self.color}'

    def __repr__(self) -> str:
        return f'{self.name=}, {self.color=}'


rex = Dog('Rex', 'Orange-Black')

a = repr(rex)

print(a)
