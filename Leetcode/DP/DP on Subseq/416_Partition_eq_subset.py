# 416. Partition Equal Subset Sum

# Recursive 
# TC = O(2^n) - At each index i, the function makes two recursive calls
# SC = O(n)
class Solution:
    def helper(self, ind, target, nums):
        # base 1
        if target == 0:
            return True
        # base 2
        if ind == 0:
            return nums[ind] == target
        if ind < 0 or target < 0:
            return False
        not_take = self.helper(ind - 1, target, nums)
        take = False
        if target >= nums[ind]:
            take = self.helper(ind - 1, target - nums[ind], nums)
        return take or not_take

    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 == 1: 
            return False
        else:
            k = total_sum // 2
            return self.helper(len(nums) -1, k, nums)

# Memoization
# TC = O(n*k) # Reason: There are N*K states therefore at max ‘N*K’ new problems will be solved.
# SC = O(n*k) + O(n)
class Solution:
    def helper(self, ind, target, nums, dp):
        # base 1
        if target == 0:
            return True
        # base 2
        if ind == 0:
            return nums[ind] == target
        if ind < 0 or target < 0:
            return False
        if dp[ind][target] != -1: return dp[ind][target]
        not_take = self.helper(ind - 1, target, nums, dp)
        take = False
        if target >= nums[ind]:
            take = self.helper(ind - 1, target - nums[ind], nums, dp)
        dp[ind][target] = take or not_take
        return dp[ind][target]

    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total_sum = sum(nums)
        if total_sum % 2 == 1: 
            return False
        else:
            k = total_sum // 2
            dp = [[-1 for _ in range(k+1)] for _ in range(n)]
            return self.helper(n -1, k, nums, dp)

# Tabulation (Bottom-up)
# TC = O(n*k) # Reason: There are N*K states therefore at max ‘N*K’ new problems will be solved.
# SC = O(n*k) 
def canPartition(n, arr):
    # Calculate the total sum of the array elements.
    totSum = sum(arr)
    
    # If the total sum is odd, it cannot be partitioned into two equal subsets.
    if totSum % 2 == 1:
        return False
    else:
        # Calculate the target sum for each subset.
        k = totSum // 2
        
        # Initialize a dynamic programming table (dp) to store subproblem results.
        dp = [[False for j in range(k + 1)] for i in range(n)]

        # Initialize the base case: An empty subset can always achieve a sum of 0.
        for i in range(n):
            dp[i][0] = True

        # Initialize the base case for the first element in the array.
        if arr[0] <= k:
            dp[0][arr[0]] = True

        # Fill in the DP table using a bottom-up approach.
        for ind in range(1, n):
            for target in range(1, k + 1):
                # If the current element is not taken, the result is the same as the previous row.
                notTaken = dp[ind - 1][target]
                
                # If the current element is taken, subtract its value from the target and check the previous row.
                taken = False
                if arr[ind] <= target:
                    taken = dp[ind - 1][target - arr[ind]]
                
                # Update the DP table with the result of taking or not taking the current element.
                dp[ind][target] = notTaken or taken
        
        # The final result is stored in the bottom-right cell of the DP table.
        return dp[n - 1][k]
