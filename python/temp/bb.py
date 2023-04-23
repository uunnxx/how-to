def trif(num):
    if num < 3:
        return 'Number must be greater than 2'

    lst = [1, 1, 1]

    for i in range(4, num+1):
        sum_of = sum(lst[i-4:i-1])
        lst.append(sum_of)

    return lst

print(*trif(7))

def trif_generator(num):
    if num < 3:
        return 'Number must be greater than 2'

    lst = [1, 1, 1]

    for i in range(4, num+1):
        sum_of = sum(lst[i-4:i-1])
        lst.append(sum_of)

    yield from lst

print(*list(trif_generator(7)))
