# 63. Unique Paths II

# Recursion
'''
Time Complexity: `O(2^(m + n)`**
- The function `f(m, n)` explores two paths at each step: **up** and **left**.
- Without memoization, this leads to an **exponential number of recursive calls, 
roughly `2^(m + n)` in the worst case.
- The presence of obstacles (`grid[m][n] == 1`) may prune some paths, but the 
worst-case complexity remains exponential.

Space Complexity: `O(m + n)`
- The space used is due to the **call stack depth** in recursion.
- In the worst case, the recursion goes from `(m, n)` to `(0, 0)`, so the maximum 
depth is `m + n`.
'''
class Solution:
    def f(self, m, n, grid):
        if m == 0 and n == 0:
            return 1
        if m < 0 or n < 0 or grid[m][n] == 1:
            return 0
        up = self.f(m - 1, n, grid)
        left = self.f(m, n - 1, grid)
        return up + left
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        return self.f(m - 1, n - 1, obstacleGrid)

# Memoization
# TC = O(m*n) Reason: At max, there will be N*M calls of recursion.
# SC = O((M-1)+(N-1)) + O(N*M)
# Reason: We are using a recursion stack space:O((M-1)+(N-1)), here (M-1)+(N-1) 
# is the path length and an external DP Array of size m*n
class Solution:
    def f(self, m, n, dp, obstacleGrid):
        """
        Recursively computes the number of unique paths considering obstacles,
        using memoization to store intermediate results.
        """
        # Base Case: If we reach the top-left corner, return 1 valid path
        if m == 0 and n == 0:
            return 1
        
        # Edge Case: If out of bounds or current cell has an obstacle, return 0
        if m < 0 or n < 0 or obstacleGrid[m][n] == 1:
            return 0
        
        # If already computed, return cached result
        if dp[m][n] != -1:
            return dp[m][n]
        # Recursive calls: Move left and move up
        # The condition if m > 0 else 0 ensures that we don't attempt to access 
        # an invalid index in the dp array when calling dp[m - 1][n].
        up = self.f(m - 1, n, dp, obstacleGrid) if m > 0 else 0
        left = self.f(m, n - 1, dp, obstacleGrid) if n > 0 else 0
        # Memoize result
        dp[m][n] = up + left
        return dp[m][n]
    

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        Initializes DP table and calls the recursive function to compute unique paths.
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # **Fix:** If the starting position has an obstacle, return 0 immediately
        if obstacleGrid[0][0] == 1:
            return 0
        dp = [[-1] * n for _ in range(m)]  # DP table initialized to -1
        return self.f(m - 1, n - 1, dp, obstacleGrid)
    
# Tabulation

# TC = O(m*n) Reason: There are two nested loops
# SC = O(m*n) Reason: We are using an external array of size m*n.
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        Computes the number of unique paths avoiding obstacles using tabulation.
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        # Edge Case: If start position has an obstacle, no paths exist
        if obstacleGrid[0][0] == 1:
            return 0
        # Initialize DP table
        dp = [[0] * n for _ in range(m)]

        # Iterating over the grid 
        for i in range(m):
            for j in range(n):
                # Base Case: If at the start position, set to 1
                if i == 0 and j == 0:
                    dp[i][j] = 1
                    continue
                
                # If current cell has an obstacle, set to 0 and continue
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue

                # Paths coming from above (if valid)
                up = dp[i-1][j] if i > 0 else 0
                
                # Paths coming from left (if valid)
                left = dp[i][j-1] if j > 0 else 0

                # Total paths to current cell
                dp[i][j] = up + left
        
        # Return the result from the bottom-right corner
        return dp[m-1][n-1]