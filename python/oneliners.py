# Flow-control
condition = True

if condition:
    print('True')


print('True') if condition else None


# Functions
def f(x):
    return f"value of {x = }"

print(f(2))


lmbd = lambda x: f"value of {x = }"
exec("def fun(x):\n    return f'value of {x = }'")

print(lmbd(2))
print(fun(4))


# Comprehensions
squares = []
for i in range(10):
    squares.append(i**2)

squares = [i**2 for i in range(10)]


# swap value of variables
def swap(x, y):
    x = x ^ y
    y = x ^ y
    x = x ^ y
    return x, y

swap(10, 20)
x, y = 10, 20
x, y = y, x


# Multiple Assignment
a, b, c = 1, 'str', 3


# Write to file
text = 'Lorem ipsum'
file_name = 'lorem.txt'

f = open(file_name, 'a')
f.write(text)
f.close()

print(text, file=open(file_name, 'a'))



