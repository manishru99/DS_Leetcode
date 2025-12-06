# 167 Two sum 2

# Rfr 1 Two sum Two pointer approach for logic

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1  # Use 0-based indexing for access
        while l < r:
            sum1 = numbers[l] + numbers[r]
            if sum1 == target:
                return [l + 1, r + 1]  # Convert result to 1-based indexing
            elif sum1 < target:
                l += 1
            else:
                r -= 1
        return [-1, -1]