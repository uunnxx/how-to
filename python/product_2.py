def max_arr_prod(arr: list):
    max_p, min_p = 1, 1

    for sub_arr in arr:
        max_el = max(sub_arr)
        min_el = min(sub_arr)

        a = max_p * max_el
        b = min_p * max_el
        c = max_p * min_el
        d = min_p * min_el

        max_p = max(a, b, c, d)
        min_p = min(a, b, c, d)

    # ????
    return max(max_p, min_p)
