def flatten(lst) -> list:
    result = []
    for item in lst:
        if isinstance(item, (list, tuple)):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

# -----------------------------------------------------------------------------

def iter_flatten(iterable):
    it = iter(iterable)
    for el in it:
        if isinstance(el, (list, tuple)):
            for f in iter_flatten(el):
                yield f
            else:
                yield el


res = []
for i in range(10):
    res = [res, i]

res = [i for i in iter_flatten(res)]

# print(res)

# -----------------------------------------------------------------------------

def flatten(l, ltypes=(list, tuple)):
    ltype = type(l)
    l = list(l)
    i = 0
    while i < len(l):
        while isinstance(l[i], ltypes):
            if not l[i]:
                l.pop(i)
                i -= 1
                break
            else:
                l[i:i + 1] = l[i]
        i += 1
    return ltype(l)


res = flatten(res)
print(res)
