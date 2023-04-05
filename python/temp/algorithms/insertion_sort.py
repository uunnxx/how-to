lst = [1, 8, 5, 2, 4, 3, 6]


# Time Complexity O(n^2)

def insertion_sort(lst):
    n = len(lst)                        # <- O(1)
    for i in range(1, n):               #             <|
        key = lst[i]                    # <- O(1)      | O(n)
        j = i - 1                       # <- O(1)     <|

        while j >= 0 and lst[j] > key:  #             <|
            lst[j + 1] = lst[j]         # <- O(1)      | O(n)
            j = j - 1                   # <- O(1)     <|

        lst[j + 1] = key                # <- O(1)
