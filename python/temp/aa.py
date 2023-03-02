def my_min(*args):
    min_of = args[0]

    for i in args[1:]:
        if i < min_of:
            min_of = i

    return min_of


print(my_min(8, 13, 4, 42, 120, 7))


def power(x, y):
    if y == 0:
        return 1
    else:
        return x * power(x, y-1)

print(power(2, 3))

hh = 'Hello'
print(hh[::-1])


def get_sum(x):
    carry = 0

    for i in range(x):
        carry += i
        yield i + carry + 1


print(*list(i for i in get_sum(5)))


def valid_paretheses(string):
    valid = True
    stack = []
    for i in string:
        if i == '(' or i == '{' or i == '[':
            stack.append(i)
        elif i == ')':
            left = stack.pop()
            if left != '(':
                valid = False
        elif i == '}':
            left = stack.pop()
            if left != '{':
                valid = False
        elif i == ']':
            left = stack.pop()
            if left != '[':
                valid = False

    return True if valid and not stack else False


print(valid_paretheses('(())((()())())'))
