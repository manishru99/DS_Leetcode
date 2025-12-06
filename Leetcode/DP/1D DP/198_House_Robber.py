# 198. House Robber 

# Recursive solution
# TC = O(2^n) SC = O(n)
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        def f(ind, nums):
            # base 1
            if ind == 0: return nums[ind]
            # base 2 (edge case)
            if ind < 0: return 0
            # pick
            pick = nums[ind] + f(ind - 2, nums)
            # not pick
            not_pick = 0 + f(ind - 1, nums)
            return max(pick, not_pick)
        return f(n-1, nums)
    
# This is also a valid recursive sol
# Moving from ind 0 to end
class Solution:
    def f(self, ind, nums, n):
        #base
        if ind >= n: return 0

        not_take = 0 + self.f(ind + 1, nums, n)
        # if take then skip next ind
        take = nums[ind] + self.f(ind + 2, nums, n)
        return max(not_take, take)

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        return self.f(0, nums, n)
        
    
# Memoization solution
# TC = O(n) 
# SC = O(n) array + O(n) for recursion stack
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        def f(ind, nums, dp):
            # base 1
            if ind == 0: return nums[ind]
            # base 2 (edge case)
            if ind < 0: return 0
            if dp[ind] != -1: return dp[ind]
            # pick
            pick = nums[ind] + f(ind - 2, nums, dp)
            # not pick
            not_pick = 0 + f(ind - 1, nums, dp)
            dp[ind] = max(pick, not_pick)
            return dp[ind]
        dp = [-1] * n
        return f(n-1, nums, dp)
'''ABove if at return dp[ind] we return dp[n - 1],
You're returning the cached result at index n - 1, which is not necessarily 
the optimal solution for the whole problem.
Instead, you should return the result computed for index ind, which is the
current position in the recursion. That value represents the maximum loot 
achievable from index ind onward.
'''
    
# Tabulation
# TC = O(n) SC = O(n)
def solveUtil(n, arr, dp):
    # Initialize the first element of the DP table with the first element of the array
    dp[0] = arr[0]
    
    # Loop through the array starting from the second element
    for i in range(1, n):
        # Calculate the maximum value when picking the current element
        pick = arr[i]
        
        # edge case
        # Check if there are at least two elements before the current element
        if i > 1:
            pick += dp[i - 2]
        
        # Calculate the maximum value when not picking the current element
        non_pick = 0 + dp[i - 1]
        
        # Store the maximum of the two choices in the DP table
        dp[i] = max(pick, non_pick)
    
    # Return the maximum value for the last index
    return dp[n - 1]

# Tabulation sol 2
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0] # only 1 elem in nums arr
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(0 + dp[i - 1], nums[i] + dp[i - 2])
        return dp[n - 1]

# Function to solve the problem for the given array
def solve(n, arr):
    # Initialize a DP table with -1 values to store intermediate results
    dp = [-1 for _ in range(n)]
    
    # Call the solveUtil function to find the maximum value
    return solveUtil(n, arr, dp)

# Space Optimized 
# TC = O(n) SC = O(1)
def rob(self, nums: List[int]) -> int:
    n = len(nums)
    def f(n, nums):
        prev = nums[0]
        prev2 = 0
        for i in range(1, n):
            # pick
            pick = nums[i]
            if i > 1: pick += prev2
            # not pick
            not_pick = 0 + prev
            curi = max(pick, not_pick)    
            prev2 = prev
            prev = curi
        return prev

    return f(n, nums)

# Or simply use without the function (rfr striver sol)