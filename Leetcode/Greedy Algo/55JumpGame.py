# Jump Game

class Solution:
    # Greedy Approach
    # TC = O(n) SC = O(1)
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        maxInd = 0
        for i, num in enumerate(nums):
            if i > maxInd:
                return False
            
            # update maxInd
            maxInd = max(maxInd, i + num)
            if maxInd >= n - 1:
                return True
        return True 

    ''' THis is same as the last one
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0  # Initialize the farthest point you can reach

        for i, num in enumerate(nums):
            if i > max_reach:  # If the current index is beyond max_reach, return False
                return False
            max_reach = max(max_reach, i + num)  # Update max_reach

            if max_reach >= len(nums) - 1:  # If you can reach or pass the last index, return True
                return True

        return False
        '''
# Space Optimized Approach
# This approach works by checking if we can reach the last index from the end of the array.
# It iterates backward and updates the target index to the current index if we can reach it from the current position.
# This way, we only need to check if we can reach the start of the array from the end.

# TC = O(n) SC = O(1)
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1: return True
        if nums[0] == 0: return False  # If the first element is 0, we cannot move anywhere
        target = n-1  #4th index

        for i in range(n-2, -1, -1):
            if(nums[i] + i >= target):
                target = i
        # If we can reach the start of the array, return True
        return target == 0
        

# DP
# Menoization Top-Down DP
'''
Time Complexity:
- Worst case: Each index calls multiple recursive branches → O(N^2).
- Optimized with memoization, reducing redundant calls → O(N) in practice.
Space Complexity:
- O(N) due to recursion depth and memoization storage.
'''
from functools import lru_cache

class Solution:
    def canJump(self, nums):
        n = len(nums)
        
        # Memoized recursive function to check if we can reach last index
        @lru_cache(None)
        def dp(pos):
            if pos >= n - 1:  # Base case: Reached last index
                return True
            
            # Try jumping within allowed range
            for jump in range(1, nums[pos] + 1):
                if dp(pos + jump):
                    return True
            
            return False  # If no valid jump found, return False
        
        return dp(0)  # Start recursion from index 0
'''
- Define a recursive function that checks if we can reach the end.
- Use memoization to avoid redundant calculations.
- Recursively explore all possible jumps from the current index.

We aim to check if we can reach the last index (4), starting from index 0, using recursion with memoization.
Recursive Calls & Memoization Table
- Start at index 0 (value 2) → Can jump +1 or +2
- Recursive call to index 1
- Recursive call to index 2
- Store the result for index 0 after exploring.
- At index 1 (value 3) → Can jump +1, +2, +3
- Recursive call to index 2, 3, and 4.
- Memoize result of index 1.
- At index 2 (value 1) → Can jump +1
- Recursive call to index 3.
- Memoize result of index 2.
- At index 3 (value 1) → Can jump +1
- Recursive call to index 4.
- Memoize result of index 3.
- At index 4 (last index) → Base Case: Return True
- Backpropagate results.
- Memoization prevents unnecessary recalculations.


'''
        
# Bottom-Up DP (Tabulation)
# 
class Solution:
    def canJump(self, nums):
        n = len(nums)
        dp = [False] * n
        dp[0] = True  # First index is always reachable
        
        for i in range(n):
            if dp[i]:  # If current index is reachable
                for j in range(1, nums[i] + 1):  # Try all jumps from current position
                    if i + j < n:
                        dp[i + j] = True  # Mark reachable index

        return dp[-1]  # Check if last index is reachable
'''
- Use a boolean DP array where dp[i] stores whether index i is reachable.
- Iterate forward, marking reachable indices using past jumps.
- The last element of the DP array will indicate if the last index is reachable.

Time Complexity:
- O(N^2) worst case (traversing jumps for every index).
- Optimized in many cases, but slower than greedy approaches.
Space Complexity:
- O(N) due to the dp array.

- Define a DP Array (dp) where dp[i] represents whether index i is reachable.
- Initialize dp[0] = True because we always start at index 0.
- Iterate through the array and update reachable positions:
- If dp[i] is True, mark all indices within nums[i] steps as reachable.
- Check the last index (dp[-1]) to determine if it's reachable.

Example Execution (nums = [2,3,1,1,4])
- Initialize DP array: [True, False, False, False, False]
- Update reachable indices:
- Index 0 (jump 2) → dp[1] = True, dp[2] = True
- Index 1 (jump 3) → dp[2] = True, dp[3] = True, dp[4] = True
- Index 2 (jump 1) → dp[3] = True
- Index 3 (jump 1) → dp[4] = True
- Final DP array: [True, True, True, True, True]
- Last index (dp[4]) is True, so return True.

'''