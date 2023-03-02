a = "возможно-это будет полезно"
r = iter(a)

while (current := next(r)) != " ":
    # print(next(r), end="")
    print(current, end="")
