from itertools import permutations


inp_1 = input()
inp_2 = int(input())

l1 = list(permutations(str(inp_2)))
l2 = []
res = ''

for i in range(len(l1)):
    for j in range(len(l1[0])):
        res += l1[i][j]
    l2.append(int(res))
    res = ''

l2.sort()

print(str(l2[1]))
