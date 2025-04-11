lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def group_by_and_reverse(lst, by):
    grouped = []
    len_of = len(lst)
    idx = 0
    temp = []
    while True:
        if (len_of - idx) >= by:
            for _ in range(by):
                temp.append(lst[idx])
                idx += 1
            grouped.extend(reversed(temp))
            temp = []
        else:
            for i in lst[idx:]:
                temp.append(i)
            grouped.extend(reversed(temp))
            break

    return grouped


print(group_by_and_reverse(lst, 7))


def group_by(lst: list, by: int) -> list:
    grouped = []
    len_of = len(lst)
    idx = 0
    temp = []
    while True:
        if (len_of - idx) >= by:
            for _ in range(by):
                temp.append(lst[idx])
                idx += 1
            grouped.append(temp)
            temp = []
        else:
            for i in lst[idx:]:
                temp.append(i)
            grouped.append(temp)
            break

    return grouped


print(group_by(lst, 7))

# a = group_by(lst, 7)
#
# print(a)

a = [[1, 2, 3], [4, 5, 6]]


print(list(map(reversed, a)))
