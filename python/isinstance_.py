class Fruit:
    def __init__(self, name: str):
        self.name = name


apple: Fruit = Fruit('Apple')
banana: Fruit = Fruit('Banana')

print(isinstance(apple, Fruit))
print(isinstance(banana, Fruit))
print(isinstance('str', str))
print(isinstance(10, int))
print(isinstance((1,), tuple))
print(isinstance([1], list))


print()

def test():
    return 0


print(isinstance(test(), str))
