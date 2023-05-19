ford = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 2023,
    'transmission': 'Automatic'
}

for item in ford:
    print(item)

print()

for key, value in ford.items():
    print(f"[{key}] {value}")

print()

for key in ford.keys():
    print(key)

print()

for value in ford.values():
    print(value)

print()

x = ('first', 'second', 'third')
y = enumerate(x)


for index, value in y:
    print(index, value)
