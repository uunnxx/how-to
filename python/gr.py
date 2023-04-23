def gr(arr):
    greatest_distance = 0
    hashmap = {}
    for i, v in enumerate(arr):
        if v not in hashmap:
            hashmap[v] = [i]
        else:
            hashmap[v].append(i)

    for cond in hashmap.values():
        for i in range(len(cond)):
            temp_res = cond[-1] - cond[i]
            if temp_res > greatest_distance:
                greatest_distance = temp_res

    return greatest_distance


print(gr([0, 2, 1, 2, 4, 1]))
print()
print(gr([9,7,1,2,3,7,0,-1,-2]))
print()
print(gr([0,7,0,2,3,7,0,-1,-2]))
