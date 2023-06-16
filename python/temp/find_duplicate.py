def findDuplicate(nums: list[int]) -> int:
    set_ = set(nums)
    sum_of_list = sum(nums)
    sum_of_sets = sum(set_)
    len_of_list = len(nums)
    len_of_sets = len(set_)
    difference = len_of_list - len_of_sets

    if difference == 1:
        return sum_of_list - sum_of_sets

    return (sum_of_list - sum_of_sets) // difference


print(findDuplicate([1, 4, 4, 2, 4]))
print(findDuplicate([2, 7, 6, 5, 1, 1, 3, 1]))
