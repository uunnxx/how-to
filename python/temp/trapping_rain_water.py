# height = [-1, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1, 0]
height = [4, 2, 0, 3, 2, 5]
output = 6


for i, e in enumerate(height):
    trap = 0

# print(max(height))
# print(height.count(max(height)))


def get_left(lst):
    for i, e in enumerate(lst):
        if e < 1:
            continue
        else:
            return lst[i:]


left = get_left(height)
print(get_left(left[::-1])[::-1])
