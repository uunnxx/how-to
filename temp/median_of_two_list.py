from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_list = sorted(nums1 + nums2)
        len_of = len(merged_list)
        if len_of % 2 == 0:
            left_mid = (len_of // 2) - 1
            right_mid = left_mid + 1
            return (merged_list[left_mid] + merged_list[right_mid]) / 2
        else:
            print('odd')
            mid = len_of // 2
            return merged_list[mid]


m = Solution()
a = m.findMedianSortedArrays([1, 2], [3, 4])
print(a)
