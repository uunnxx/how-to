class Solution:
    def containsDuplicate(self, nums: list[int]):
        # set_: set = set()
        #
        # len_of_nums = len(nums)
        # sqrt_of_nums = round(len_of_nums**.5)
        # range_ = len_of_nums // sqrt_of_nums
        #
        # for i in range(range_ + 1):
        #     iter_start = i * sqrt_of_nums
        #     iter_end = sqrt_of_nums * (i + 1)
        #     iter_range = nums[iter_start:iter_end]
        #
        #     given = len(set_)
        #
        #     for v in iter_range:
        #         print(nums[iter_start:iter_end])
        #         set_.add(v)
        #
        #     expected = given + len(iter_range)
        #     got = len(set_)
        #
        #     print(f"{expected = } {got = }")
        #
        #
        #
        #     if got != expected:
        #         return True
        #
        # return False
        return not len(set(nums)) == len(nums)


# n = [1, 2, 3, 4, 4, 5, 7, 8, 0, 9, 6]
n = [1, 2, 3, 2]
# n = [2,14,18,22,22]

ss = Solution()
print(ss.containsDuplicate(n))
