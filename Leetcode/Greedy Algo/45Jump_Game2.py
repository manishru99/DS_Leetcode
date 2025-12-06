# 45. Jump Game II

# TC = O(k^n), where k is the maximum jump length and  is the size of the array. 
# SC = O(n)
class Solution:
    def num_jumps(self, ind, nums):
        # Base case: If the current index has reached or exceeded the last index
        if ind >= len(nums) - 1:
            return 0  # No more jumps needed
        
        # If the current position has zero steps, it's a dead end
        if nums[ind] == 0:
            return float('inf')  # Impossible to jump further

        # Try all possible jumps from 1 to nums[ind]
        min_jumps = float('inf')  # Initialize to infinity
        for jump in range(1, nums[ind] + 1):
            # Recursive call to find the jumps for the next indices
            min_jumps = min(min_jumps, 1 + self.num_jumps(ind + jump, nums))

        return min_jumps

    def jump(self, nums):
        return self.num_jumps(0, nums)
    
# Solution 2 Memoization
# TC = O(n^2) (due to the recursive calls and the inner loop).
# SC = O(n) + O(n) for the memoization array and recursion stack
class Solution:
    def num_jumps(self, ind, nums, dp):
        # Base case: If the current index has reached or exceeded the last index
        if ind >= len(nums) - 1:
            return 0  # No more jumps needed
        
        # If the current position has zero steps, it's a dead end
        if nums[ind] == 0:
            return float('inf')  # Impossible to jump further
        if dp[ind] != -1:
            return dp[ind]

        # Try all possible jumps from 1 to nums[ind]
        min_jumps = float('inf')  # Initialize to infinity
        for jump in range(1, nums[ind] + 1):
            # Recursive call to find the jumps for the next indices
            min_jumps = min(min_jumps, 1 + self.num_jumps(ind + jump, nums, dp))
        dp[ind] = min_jumps # Store the result in dp arr
        return min_jumps

    def jump(self, nums):
        n = len(nums)
        dp = [-1] * n
        return self.num_jumps(0, nums, dp)

# Solution 3 Tabulation
# TC = O(n^2) SC = O(n)
def jump(nums):
    n = len(nums)
    dp = [float('inf')] * n  # Initialize dp array with infinity
    dp[0] = 0  # Starting point, no jumps needed

    for i in range(n):
        for jump in range(1, nums[i] + 1):
            if i + jump < n:
                dp[i + jump] = min(dp[i + jump], dp[i] + 1)

    return dp[-1]  # Return the minimum jumps to reach the last index

# Solution 4 Greedy approach
# TC = O(n) SC = O(1)
def jump(self, nums: List[int]) -> int:
    n = len(nums)
    
    # Initialize the boundaries of the current "jump range"
    # 'l' represents the start of the range, 'r' represents the end of the range
    l, r = 0, 0
    jumps = 0
    
    # Continue jumping until the end of the array is reached
    while r < n - 1:
        # Variable to keep track of the farthest position reachable in the current range
        farthest = 0

        # Loop through the current range (from 'l' to 'r') to calculate the farthest position
        for ind in range(l, r + 1):
            # Update farthest reachable index using the current position and maximum jump length
            farthest = max(farthest, ind + nums[ind])
        
        # Update the start of the range to the end of the previous range
        l = r + 1

        # Increment the number of jumps as we're moving to the next range
        jumps += 1

        # Update the end of the current range to the farthest reachable index
        r = farthest
    
    # Return the total number of jumps required to reach the end
    return jumps









'''
Dry Run of Recursive Approach on nums = [2,3,1,1,4]
This approach uses recursion to find the minimum number of jumps needed to reach the last index.
We start at index 0 and recursively explore all possible jumps.

Recursive Calls Breakdown
Step 1: Start at index 0 (value 2)
- Possible jumps: +1 or +2
- Recursive calls:
- num_jumps(1, nums)
- num_jumps(2, nums)

Step 2: At index 1 (value 3)
- Possible jumps: +1, +2, +3
- Recursive calls:
- num_jumps(2, nums)
- num_jumps(3, nums)
- num_jumps(4, nums)

Step 3: At index 2 (value 1)
- Possible jumps: +1
- Recursive call:
- num_jumps(3, nums)

Step 4: At index 3 (value 1)
- Possible jumps: +1
- Recursive call:
- num_jumps(4, nums)

Step 5: At index 4 (last index)
- Base Case: ind >= len(nums) - 1
- Return 0 (no more jumps needed)

Final Computation
- num_jumps(4) = 0
- num_jumps(3) = 1 + 0 = 1
- num_jumps(2) = 1 + 1 = 2
- num_jumps(1) = min(1 + 2, 1 + 1, 1 + 0) = min(3, 2, 1) = 1
- num_jumps(0) = min(1 + 1, 1 + 2) = min(2, 3) = 2

Time Complexity Analysis of Recursive Approach
- Recursive Calls:
- At each index, we explore all possible jumps (nums[ind] choices).
- In the worst case, each index makes multiple recursive calls, leading to exponential growth.
- Worst Case Scenario (nums = [1,1,1,1,...]):
- Each index calls the next index recursively.
- Forms a recursive tree with O(2^N) complexity in the worst case.
- Optimized Case (nums = [N,0,0,0,...]):
- If the first element allows jumping directly to the end, only O(1) calls are made.
Total Time Complexity (Worst Case):
[ O(2^N) ]
This is exponential, making it highly inefficient for large inputs.


DRY run for Memoization:
Memoization Table Updates
| Index | Computation | Stored in dp | 
| 4 | Base Case → 0 | dp[4] = 0 | 
| 3 | 1 + dp[4] = 1 | dp[3] = 1 | 
| 2 | 1 + dp[3] = 2 | dp[2] = 2 | 
| 1 | min(1 + dp[2], 1 + dp[3], 1 + dp[4]) = min(3, 2, 1) = 1 | dp[1] = 1 | 
| 0 | min(1 + dp[1], 1 + dp[2]) = min(2, 3) = 2 | dp[0] = 2 | 


DRY run for tabulation:
Iterate over index i = 0 (nums[0] = 2)
- Possible jumps: +1 or +2
- Update:
- dp[1] = min(dp[1], dp[0] + 1) → min(inf, 0 + 1) = 1
- dp[2] = min(dp[2], dp[0] + 1) → min(inf, 0 + 1) = 1
Updated DP array: [0, 1, 1, inf, inf]

Iterate over index i = 1 (nums[1] = 3)
- Possible jumps: +1, +2, +3
- Update:
- dp[2] = min(dp[2], dp[1] + 1) → min(1, 1 + 1) = 1 (No change)
- dp[3] = min(dp[3], dp[1] + 1) → min(inf, 1 + 1) = 2
- dp[4] = min(dp[4], dp[1] + 1) → min(inf, 1 + 1) = 2
Updated DP array: [0, 1, 1, 2, 2]

Iterate over index i = 2 (nums[2] = 1)
- Possible jump: +1
- Update:
- dp[3] = min(dp[3], dp[2] + 1) → min(2, 1 + 1) = 2 (No change)
Updated DP array: [0, 1, 1, 2, 2]

Iterate over index i = 3 (nums[3] = 1)
- Possible jump: +1
- Update:
- dp[4] = min(dp[4], dp[3] + 1) → min(2, 2 + 1) = 2 (No change)
Updated DP array: [0, 1, 1, 2, 2]

Final Result
- dp[-1] = 2, meaning minimum jumps to reach the last index is 2.

Time Complexity Analysis
- Outer Loop (for i in range(n)) → O(N)
- Iterates through all indices in the array.
- Inner Loop (for jump in range(1, nums[i] + 1)) → O(N) in the worst case
- In the worst case, nums[i] can be up to N, leading to O(N) operations per index.
- This results in O(N²) complexity in worst-case scenarios.
Total Time Complexity:
[ O(N^2) ] Since each index processes multiple jumps, but memoization prevents redundant recalculations.

Space Complexity Analysis
- DP Array (dp) → O(N)
- Stores the minimum jumps required for each index.
- No Additional Recursive Calls
- Since this is a bottom-up iterative approach, there is no recursion overhead.
Total Space Complexity:
[ O(N) ] due to storing the dp array.


'''