# Frog Jump GFG DP 3
# Note: In memoization we dont require helper function as we are using dp array to store the results of subproblems.
# We can directly use the results to calculate the final result.
# But helper function can also be used.

# Recursive approach
# TC = O(2^n) SC = O(n)
class Solution:
    def f(self, n, height):
        # Base case: If the step is the first one, cost is 0
        if n == 0:
            return 0
        if n == 1:
            return abs(height[1] - height[0])  # Only one jump available
        
        # Recursive case: Choose between the last two possible jumps
        left = self.f(n - 1, height) + abs(height[n] - height[n - 1])
        right = self.f(n - 2, height) + abs(height[n] - height[n - 2])
        
        return min(left, right)
    
    def minCost(self, height):
        n = len(height) - 1  # Start from the last index
        return self.f(n, height)
    
# Memoization
# TC = O(n) Due to overlapping subproblems
# SC = O(n) + O(n) for dp arr and recursion stack
class Solution:
    def f(self, n, height, dp):
        if n == 1:
            return 0  # Starting point, no cost
        if dp[n] != -1:
            return dp[n]
        
        # Calculate the cost of one jump
        left = self.f(n - 1, height, dp) + abs(height[n - 1] - height[n - 2])
        
        # Note: for n=2, n > 2 is false, the right path remains float('inf').
        # Calculate the cost of two jumps only if n > 2
        right = float('inf')  # Default to infinity if two-jump isn't possible
        if n > 2:
            right = self.f(n - 2, height, dp) + abs(height[n - 1] - height[n - 3])
        
        # Store the minimum cost in dp array
        dp[n] = min(left, right)
        return dp[n]

    def minCost(self, height):
        n = len(height)  # Correct the indexing for 0-based list
        dp = [-1] * (n + 1)  # Use n+1 for 1-based indexing in `f` # rfr striver correct solution
        return self.f(n, height, dp)

# Tabulation
# TC = O(n) SC = O(n) 
def minCost(self, height):
    n = len(height)  
    # Tabulation (bottom up)
    dp = [-1] * n  # Allocate dp array with size n
    dp[0] = 0  # Base case: cost to reach the first step is 0
    for i in range(1, n):
        # First step cost
        fs = dp[i-1] + abs(height[i] - height[i-1])
        ss = float('inf')  # Initialize second step cost to infinity
        if i > 1:  # Ensure i-2 is a valid index
            # Second step cost
            ss = dp[i-2] + abs(height[i] - height[i-2])
        dp[i] = min(fs, ss)  # Choose the minimum cost for the current step
    return dp[n-1]  # Minimum cost to reach the last step


# Space Optimization
# TC = O(n) SC = O(1)
def minCost(self, height):
    n = len(height) 
    prev = 0
    prev2 = 0
    for i in range(1, n):
        # first step
        fs = prev + abs(height[i] - height[i-1])
        ss = float('inf')
        if i > 1:
            #second step
            ss = prev2 + abs(height[i] - height[i-2])
        curr_i = min(fs, ss)
        prev2 = prev
        prev = curr_i
    return prev

