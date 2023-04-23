from itertools import permutations


inp_1 = input()
inp_2 = int(input())

l1 = list(permutations(str(inp_2)))
l2 = []
res = ''

for item in l1:
    for j in range(len(l1[0])):
        res += item[j]
    l2.append(int(res))
    res = ''

l2.sort()

print(l2[1])
