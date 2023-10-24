class Solution:
    def contains_duplicate(self, nums: list[int]) -> bool:
        # dict_: dict = {}

        # for i in nums:
        #     if dict_.get(i, None):
        #         dict_[i] += 1
        #     else:
        #         dict_[i] = 1

        # for i in dict_.values():
        #     if i > 1:
        #         return True

        # return False
        # for i in nums:
        #     if dict_.get(i, None):
        #         return True
        #     else:
        #         dict_[i] = 1

        # return False

        # hashset = set()
        # len_of_nums = len(nums)**0.5

        # def _perform(index, value):
        #     if index == len_of_nums:
        #         pass

        #     before = len(hashset)
        #     hashset.add(v)
        #     after = len(hashset)

        #     if before == after:
        #         return True

        # for i, v in enumerate(nums[:-len_of_nums]):
        #     _perform(i, v)

        # return False

        # set_: set = set()

        # len_of_nums = len(nums)
        # sqrt_of_nums = round(len_of_nums**.5)
        # range_ = len_of_nums // sqrt_of_nums

        # for i in range(range_ + 1):
        #     iter_start = i * sqrt_of_nums
        #     iter_end = sqrt_of_nums * (i + 1)
        #     iter_range = nums[iter_start:iter_end]

        #     given = len(set_)
        #     for v in iter_range:
        #         set_.add(v)

        #     expected = given + len(iter_range)
        #     got = len(set_)

        #     if got != expected:
        #         return True

        # return False
        # O(n)
        return not len(set(nums)) == len(nums)


test = [1, 2, 3, 4]

s1 = Solution()
print(s1.contains_duplicate(test))


# O(nlogn)
class SolutionWithSort:
    def contains_duplicate(self, lst: list[int]) -> bool:
        sorted_list = sorted(lst)

        temp_val = None
        for _, v in enumerate(sorted_list):
            if temp_val == v:
                return True
            temp_val = v
        return False


s2 = SolutionWithSort()
print(s2.contains_duplicate(test))



class SolutionWithSort2:
    def contains_duplicate(self, lst: list[int]) -> bool:
        lst.sort()

        for i in range(1, len(lst)):
            if lst[i-1] == lst[i]:
                return True
        return False


s21 = SolutionWithSort2()
print(s21.contains_duplicate(test))



# O(n)
class SolutionWithHashSet:
    def contains_duplicate(self, lst: list[int]) -> bool:
        hashset = set()

        for n in lst:
            if n in hashset:
                return True
            hashset.add(n)

        return False



s3 = SolutionWithHashSet()
print(s3.contains_duplicate(test))




