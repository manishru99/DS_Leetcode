# 300. Longest Increasing Subsequence

# Recursion
# TC = O(2^n) (as we have 2 x 2 x 2 x ... options for every elem)
# SC = O(n)
class Solution:
    def f(self, ind, prev, nums, n):
        # base
        if ind == n: return 0
        not_take = 0 + self.f(ind + 1, prev, nums, n)
        take = 0
        if prev == -1 or nums[ind] > nums[prev]: 
            take = 1 + self.f(ind + 1, ind, nums, n)
        maxl = max(not_take, take)
        return maxl
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        return self.f(0, -1, nums, n)
    
# Memoization
# Coordinate shift and recursion tree rfr striver notes
# TLE error on LC
class Solution:
    def f(self, ind, prev, nums, n, dp):
        # base
        if ind == n: return 0
        if dp[ind][prev + 1] != -1: return dp[ind][prev + 1]
        not_take = 0 + self.f(ind + 1, prev, nums, n, dp)
        take = 0
        if prev == -1 or nums[ind] > nums[prev]: 
            take = 1 + self.f(ind + 1, ind, nums, n, dp)
        dp[ind][prev + 1] = max(not_take, take)
        return dp[ind][prev + 1]
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1 for _ in range(n + 1)] for _ in range(n)]
        return self.f(0, -1, nums, n, dp)
    
# Tabulation
''' TC = O(n^2) - - The outer loop runs for ind from n-1 down to 0 → O(n)
- The inner loop runs for prev from ind-1 to -1 → up to O(n) in the worst case
SC = O(n^2) -- Your dp table is of size (n+1) × (n+1) → O(n²)
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0 for _ in range(n + 1)] for _ in range(n+1)]
        for ind in range(n - 1, -1, -1):
            for prev in range(ind - 1, -2, -1):
                not_take = dp[ind + 1][prev + 1]
                take = 0
                if prev == -1 or nums[ind] > nums[prev]:
                    take = 1 + dp[ind + 1][ind + 1]
                dp[ind][prev + 1] = max(take, not_take)
        return dp[0][0]
        
'''
Why in tabulation while declaring dp the index goes from 0 to n in for loop but in memorization it goes from 0 to n-1?

Memoization (Top-Down)
In memoization:
- You build your logic around valid input indices, typically from 0 to n-1.
- The recursive call defines the base case, like if ind == n: return 0, so index n is a termination point, not an actual state you compute.
- Therefore, your dp table only needs to store values from 0 to n-1, hence dp = [[-1] * (n + 1) for _ in range(n)].
Think of memoization as:
“I'll solve this problem starting from index 0 and cache things only if I need them.”

Tabulation (Bottom-Up)
In tabulation:
- You're filling out the dp table iteratively, and that includes future states like dp[n][...] because they get referenced while solving smaller subproblems.
- For example, if you're solving from ind = n-1 downward, you’ll often reference dp[ind + 1][...] or even dp[ind + 2][...] (like with cooldown problems).
- So you allocate up to n+1 or n+2 rows depending on how far ahead you need to look.
In short:
“I'm going to pre-allocate the full table — including the base states I’ll rely on.”

'''


