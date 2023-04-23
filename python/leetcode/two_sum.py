# Alternative solution
# O(n^2)

class Solution:
    def twoSum(self, lst, target: int):
        curr = 0
        original = lst

        def sum_it(lst, current=1):
            nonlocal curr
            nonlocal original
            nonlocal target

            curr += current

            if len(lst) < 1:
                return 1

            for i in range(len(lst)-1):
                if lst[0] + lst[i+1] == target:
                    first = original.index(lst[0])
                    second = original.index(lst[i+1], first+1)

                    return [first, second]

            return sum_it(lst[current:])
        return sum_it(lst)


sol = Solution()
# res = sol.twoSum([2, 7, 11, 15], 9)
res = sol.twoSum([2, 7, 11, 15, 2], 4)

print(res)
