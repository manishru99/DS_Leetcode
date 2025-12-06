# 494 Target Sum
# Similar to Count Partitions with GIven Difference (DP-21)

# Recursive
# TC = O(2^n)
# SC = O(n)
class Solution:
    def f(self, ind, target, nums):
        if ind == 0:
            if target == 0 and nums[0] == 0: # handle 0 val
                return 2
            if target == 0 or target == nums[0]:
                return 1
            return 0
        
        not_take = self.f(ind - 1, target, nums)
        take = 0
        if nums[ind] <= target:
            take = self.f(ind - 1, target - nums[ind], nums)
        return not_take + take


    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        totalSum = sum(nums)
        if totalSum - target < 0: return 0
        if (totalSum - target) % 2 == 1: return 0 
        s2 = (totalSum - target) // 2
        return self.f(n-1, s2, nums)

# Memoization top-down
'''
Time Complexity: O(N*K)
Reason: There are N*K states therefore at max N*K new problems will be solved.

Space Complexity: O(N*K) + O(N)
Reason: We are using a recursion stack space(O(N)) and a 2D array ( O(N*K)).
'''
class Solution:
    def f(self, ind, target, nums, dp):
        if ind == 0:
            if target == 0 and nums[0] == 0: # handle 0 val explanation in striver DP-18 lec
                return 2
            if target == 0 or target == nums[0]:
                return 1
            return 0
        if dp[ind][target] != -1:
            return dp[ind][target]
        
        not_take = self.f(ind - 1, target, nums, dp)
        take = 0
        if nums[ind] <= target:
            take = self.f(ind - 1, target - nums[ind], nums, dp)
        dp[ind][target] = not_take + take
        return dp[ind][target]


    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        totalSum = sum(nums)
        if totalSum - target < 0: return 0
        if (totalSum - target) % 2 == 1: return 0 
        s2 = (totalSum - target) // 2
        dp = [[-1 for _ in range(s2 + 1)] for _ in range(n)]
        return self.f(n-1, s2, nums, dp)
    

# Tabulation Bottom-up
'''
Time Complexity: O(N*K)
Reason: There are two nested loops

Space Complexity: O(N*K)
Reason: We are using an external array of size N*K. Stack Space is eliminated.
'''
class Solution:
    mod = int(1e9 + 7)
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        totalSum = sum(nums)

        # Edge cases: impossible target or odd partition sum
        if totalSum - target < 0: return 0
        if (totalSum - target) % 2 == 1: return 0 

        s2 = (totalSum - target) // 2
        dp = [[0 for _ in range(s2 + 1)] for _ in range(n)]

        # Base Case Handling
        if nums[0] == 0:
            dp[0][0] = 2     # `{+0, -0}` both contribute
        else:
            dp[0][0] = 1    # Only one way to form sum 0
        if nums[0] != 0 and nums[0] <= s2:
            dp[0][nums[0]] = 1  # One way to form `nums[0]`

        # Filling DP table
        for ind in range(1, n):
            for T in range(s2 + 1):
                not_take = dp[ind - 1][T]
                take = 0
                if nums[ind] <= T:
                    take = dp[ind-1][T - nums[ind]]
                dp[ind][T] = (not_take + take) 
        return dp[n - 1][s2]
        