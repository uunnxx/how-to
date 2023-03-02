def print_max(a, b):
    if a > b:
        print(a, 'A is maximum')
    elif a == b:
        print(a, 'A is equal to B', b)
    else:
        print(b, 'B is maximum')

# directly pass literal values
print_max(3, 4)

x = 5
y = 7

# pass variables as arguments
print_max(x, y)
