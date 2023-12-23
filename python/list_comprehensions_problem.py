x = 1
y = 1
z = 1
n = 2

# combinations = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1)]

# print(combinations)

# res = [lst for lst in combinations if sum(lst) != n]
# for i in combinations:
#     print(i)

# print(res)


print([lst for lst in [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1)] if sum(lst) != n])
