lst = [
    [2, 3, 4, 5, 6],
    [3, 2, 7, 8, 9],
    [4, 7, 2, 0, 4],
    [5, 8, 0, 2, 1],
    [6, 2, 4, 1, 4]
]

symmetric = False
length = len(lst)
counter = -(length)
sym_digit = lst[0][0]

# for row in lst:
#
#     if (len(row) != length):
#         print('NO')
#         raise SystemExit(0)
#
#     if sym_digit == row[counter + length]:
#         symmetric = True
#     else:
#         symmetric = False
#
#     counter += 1

row = 0
while (sym_digit == lst[row][counter + length]):
    if (len(lst[row]) != length):
        print('NO')
        raise SystemExit(0)

    row += 1



print('YES')
