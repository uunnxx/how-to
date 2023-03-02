class Solution:
    def addTwoNumbers(self, l1: list , l2: list):
        l1 = list(map(str, l1))
        l2 = list(map(str, l2))
        l1.reverse()
        l2.reverse()
        t = int(''.join(l1)) + int(''.join(l2))
        print(list(str(t)))


s = Solution()
s.addTwoNumbers([2, 4, 3], [5, 6, 4])


