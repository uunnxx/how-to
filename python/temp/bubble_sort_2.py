def bubble_sort(lst):
    for passnum in range(len(lst) - 1, 0, -1):
        for i in range(passnum):
            if lst[i] > lst[i + 1]:
                temp = lst[i]
                lst [i] = lst[i + 1]
                lst[i + 1] = temp
    print(lst)


lst = [54, 22, 23, 47, 23, 44, 31, 23, 76, 99]

bubble_sort(lst)
bubble_sort([54, 22, 23, 47, 23, 44, 31, 23, 16, 11])
bubble_sort([1, 337, 23, 57, 23, 84, 1, 2, 6, 11])
bubble_sort([4, 20, 79, 44, 23, 66, 31, 7, 11])
bubble_sort([31, 12, 23, 31, 23, 17, 31, 27, 716])
bubble_sort([22, 24, 33, 23, 48, 31, 7, 7])
bubble_sort([13, 77, 23, 99, 31, 197, 6])
