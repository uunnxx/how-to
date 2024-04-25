def binary_search(lst: list, low: int, high: int, x: int) -> int:
    if high >= low:
        mid = (high + low) // 2

        if lst[mid] == x:
            return mid
        elif lst[mid] > x:
            return binary_search(lst, low, mid - 1, x)
        else:
            return binary_search(lst, mid + 1, high, x)

    return -1
