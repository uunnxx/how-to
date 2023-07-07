def check_parentheses(string: str) -> bool:
    stack = []
    for c in string:
        if c == '(':
            stack.append(')')
        if c == ')':
            if len(stack) == 0:
                return False
            else:
                stack.pop()

    return len(stack) == 0



print(check_parentheses('())()'))

print(dir('aaa'))
