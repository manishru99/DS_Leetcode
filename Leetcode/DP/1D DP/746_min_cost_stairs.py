# 746. Min Cost Climbing Stairs

# Recursive
# TC = O(2^n) SC = O(n)
from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        def dfs(i):
            """
            Recursively computes the minimum cost to reach the top from stair index `i`.
            Args:
            i (int): Current stair index.
            Returns:
            int: Minimum cost from index `i` to the top.
            """
            # Base case: If we've exceeded the last step, no cost is needed.
            if i >= n: return 0
            # Recursive step:
            # - Take `cost[i]` and add the minimum cost from the next two possible moves (i+1 or i+2).
            # - This ensures we always pick the path with the least cumulative cost.
            return cost[i] + min(dfs(i + 1), dfs(i + 2))
        # Since we can start from either the 0th or 1st step, return the minimum cost from both.
        return min(dfs(0), dfs(1))

# Memoization top-down approach
# TC = O(n) SC = O(n)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = [-1] * n  # Initialize memoization array with -1 (uncomputed values)
        def dfs(i):
            # Base Case: If we've exceeded the last step, no cost is needed.
            if i >= n:
                return 0
            # If this index has been computed before, return the stored value (memoization)
            if memo[i] != -1:
                return memo[i]
            # Compute and store the minimum cost for this index in memo
            # - Option 1: Take one step (`dfs(i+1)`)
            # - Option 2: Take two steps (`dfs(i+2)`)
            memo[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
            return memo[i]

        # Since we can start from either step 0 or step 1, take the minimum of both starting points
        return min(dfs(0), dfs(1))

# Tabulation bottom-up approach
# TC = O(n) SC = O(n)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)  # Get the number of stairs
        dp = [0] * (n + 1)  # DP array to store minimum cost to reach each step
        # n + 1 to handle below cost[i-2]+dp[i-2] when i = 2 -> cost[0]+dp[0]

        # Step 1: Iterate through stairs starting from the 2nd stair (index 2)
        for i in range(2, n + 1):
            # Step 2: Compute the minimum cost for reaching step i
            # - Option 1: Step from (i-1) with cost[i-1] + previously computed cost (dp[i-1])
            # - Option 2: Step from (i-2) with cost[i-2] + previously computed cost (dp[i-2])
            # - Take the minimum of these two choices
            dp[i] = min(cost[i - 1] + dp[i - 1], cost[i - 2] + dp[i - 2])

        # Step 3: Return the minimum cost to reach the top of the stairs
        return dp[n]

''' For dp[0] and dp[1]:
- Base Case: You can start climbing from either index 0 or index 1.
- No cost is required before stepping on the first two stairs, so dp[0] = 0 and dp[1] = 0 are default values.
- First computed step (dp[2]):
dp[2] = min(cost[1] + dp[1], cost[0] + dp[0])

Here dp[1] is min cost to reach there and cost[1] is the cost at that particular ind

- Since dp[0] and dp[1] are 0, this correctly computes the minimum cost to start climbing.
'''


