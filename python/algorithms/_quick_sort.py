# N*log(N)


# Pivot -> first element
# Variants: first_element, median, random
def quick_sort(arr: list, reversed: bool = False) -> list:
    sorted_list: list = arr[:]
    rev = reversed

    if not len(sorted_list):
        return sorted_list

    pivot: int = sorted_list[0]

    if not reversed:
        left_hand = [e for e in sorted_list if e < pivot]
        right_hand = [e for e in sorted_list if e > pivot]
    else:
        left_hand = [e for e in sorted_list if e > pivot]
        right_hand = [e for e in sorted_list if e < pivot]

    return (
        quick_sort(left_hand, rev)
        + [e for e in sorted_list if e == pivot]
        + quick_sort(right_hand, rev)
    )


print(quick_sort([2, 1, 3, 1, 0, 5], reversed=True))
