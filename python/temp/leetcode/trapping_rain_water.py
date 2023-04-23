from typing import List


"""
Trapping Rain Water
Given `n` non-negative integers representing an elevation map where the width
of each bar is `1`, compute how much water it can trap after raining.


  ^
6 |
5 |
4 |
3 |                          |||
2 |          ||| +++ +++ +++ |||-||| +++ ||| -------
1 |--||| +++ |||-||| +++ |||-|||-|||-|||-|||--|||---
0 |---1---2---3---4---5---6---7---8---9---10---11---

  [0, 1,  0,  2,  1,  0,  1,  3,  2,  1,  2,   1]


Input: [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
Output: 6
Explanation: The above elevation map (||| section) is represented by
    array [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]. In this case, 6 units of
    rain water (+++ section) are being trapped.


NeetCode solution:

First:
O(n) time complexity
O(n) space complexity

Input:                 [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

Max Left:              [0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
Max Right:             [3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1, 0] in reverse input
Min(l, r):             [0, 0, 1, 1, 2, 2, 2, 2, 2, 2, 1, 0]

Min(l, r) - height:    [0, 0, 1, 0, 1, 2, 1, 0, 0, 1, 0, 0]

Second:
O(n) time complexity
O(1) space complexity

Two pointers `left` and `right`

Input:                 [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

"""


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
output = 6

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r]
        res = 0

        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                res += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                res += right_max - height[r]

        return res


sol = Solution()
assert sol.trap(height) == output, f'Should be equal to {output}'
print(f"Expected output is {output}, we got {sol.trap(height)}")


#
# trap = 0

# print(max(height))
# print(height.count(max(height)))


# def get_left(lst):
#     for i, e in enumerate(lst):
#         if e < 1:
#             continue
#         else:
#             return lst[i:]
#

# left = get_left(height)
# print(get_left(left[::-1])[::-1])
