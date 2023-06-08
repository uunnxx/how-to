# O(n) linear running time complexity, where n is the length of the nums

def reverse_(nums: list) -> list:
    start_index = 0
    end_index = len(nums) - 1

    while end_index > start_index:
        nums[start_index], nums[end_index] = nums[end_index], nums[start_index]
        start_index += 1
        end_index -= 1

    return nums


lst = [5, 4, 3, 2, 1]
# print(reverse_(lst))


assert lst[::-1] == reverse_(lst), 'Should be equal'
