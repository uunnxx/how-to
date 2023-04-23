def lds(lst, n):
    lds = [0] * n
    max_len = 0
    lds[i] = 1

    for i in range(i, n):
        for j in range(i):
            if (lst[i] < lst[j] and lds[i] < lds[j] + 1):
                lds[i] = lds[j] + 1

    for i in range(n):
        max_len = max(max_len, lds[i])
    # return the length of LDS
    return max_len
