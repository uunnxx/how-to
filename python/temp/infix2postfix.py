def infix_postfix(inp: str):
    OP = {'+', '-', '*', '/', '(', ')', '^'}
    PR = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    s = []
    res = ''

    for ch in inp:
        if ch not in OP:
            res += ch
        elif ch == '(':
            s.append('(')
        elif ch == ')':
            while s and s[-1] != '(':
                res += s.pop()
        else:
            while s and s[-1] != '(' and PR[ch] <= PR[s[-1]]:
                res += s.pop()
            s.append(ch)

    while s:
        res += s.pop()

    return res


