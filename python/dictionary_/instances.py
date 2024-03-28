class Klass:
    pass

obj = Klass()


a = [4, 0, 'string', 5.0, [2, 2], ('it', 'is', 'a', 'tuple'), obj, [1, 0]]


count = 0
lst = []

for i in a:
    print(f"{i} >>\n\t{type(i)=}\n")

    if isinstance(i, int | float):
        count += i
    elif isinstance(i, list):
        lst.extend(i)


print(count)
print(lst)
