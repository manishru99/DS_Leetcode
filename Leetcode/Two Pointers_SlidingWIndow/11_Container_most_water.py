# 11. Container With Most Water

# Brute
# TC = O(n^2) SC = O(1)
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                res = max(res, min(heights[i], heights[j]) * (j - i))
        return res

# Two pointer
# TC = O(n) SC = O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n - 1
        max_area = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            max_area = max(max_area, area)
            if height[l] < height[r]: l += 1
            else: r -= 1
        return max_area

