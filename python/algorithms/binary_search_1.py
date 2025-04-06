def binary_search(lst: list[int], item: int) -> bool:
    first = 0
    last = len(lst) - 1
    flag_found = False

    while first <= last and not flag_found:
        mid = (first + last) // 2
        if lst[mid] == item:
            flag_found = True
        else:
            if item < lst[mid]:
                last = mid - 1
            else:
                first = mid + 1

    return flag_found


print(binary_search([8, 9, 10, 12, 15, 30, 31, 543, 756], 10))
print(binary_search([8, 9, 10, 12, 15, 30, 31, 543, 756], 11))
