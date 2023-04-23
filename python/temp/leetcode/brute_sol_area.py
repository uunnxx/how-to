from typing import List


inp = [1, 8, 6, 2, 5, 4, 8, 3, 7]


class BruteForceSolution:
    """
    Brute-force solution with O(n^2) time complexity
    """

    def max_area(self, height: List[int]) -> int:
        res = 0

        for left in range(len(height)):
            for right in range(left + 1, len(height)):
                area = (right - left) * min(height[left], height[right])
                res = max(res, area)

        return res


sol = BruteForceSolution()
print(sol.max_area(inp))


class LinearSolution:
    """
    Linear solution with O(n) time complexity
    """

    def max_area(self, height: List[int]) -> int:
        res = 0
        left, right = 0, len(height) - 1
        while left < right:
            area = (right - left) * min(height[left], height[right])
            res = max(res, area)

            if height[left] < height[right]:
                left += 1
            # elif height[left] > height[right]:
            #     right -= 1
            else:
                right -= 1

        return res


sol2 = LinearSolution()
print(sol2.max_area(inp))
