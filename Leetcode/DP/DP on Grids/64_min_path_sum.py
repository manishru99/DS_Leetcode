# 64. Minimum Path Sum

# Recursive
# TC = O(2^(m+n)) SC = O(m+n)
class Solution:
    def f(self, m, n, grid):
        # base 1
        if m == 0 and n == 0: return grid[m][n]
        # edge
        if m < 0 or n < 0: return int(1e9)
        up = grid[m][n] + self.f(m-1, n, grid)
        left = grid[m][n] + self.f(m, n-1, grid)
        return min(up, left)

    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        return self.f(m-1, n-1, grid)
    
# Memoization
# TC = O(m*n)
# SC = O(m-1 + n-1) for rec st space + O(m*n) for dp arr
class Solution:
    def f(self, m, n, grid, dp):
        # base 1
        if m == 0 and n == 0: return grid[m][n]
        # edge
        if m < 0 or n < 0: return int(1e9)
        if dp[m][n] != -1: return dp[m][n]
        up = grid[m][n] + self.f(m-1, n, grid, dp)
        left = grid[m][n] + self.f(m, n-1, grid, dp)
        dp[m][n] = min(up, left)
        return dp[m][n]

    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[-1] * n for _ in range(m)]
        return self.f(m-1, n-1, grid, dp)
    
# Tabulation
# TC = O(m*n) Reason: there are 2 nested loops
# SC = O(m*n) Reason: We are using an external array of size
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[-1] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                # base 1
                if i == 0 and j == 0: 
                    dp[i][j] = grid[i][j]
                    continue
                # edge
                #if m < 0 or n < 0: return (1e9)
                # if dp[m][n] != -1: return dp[m][n]
                up = grid[i][j] + dp[i-1][j] if i > 0 else int(1e9)
                left = grid[i][j] + dp[i][j-1] if j > 0 else int(1e9)
                dp[i][j] = min(up, left)
        return dp[m-1][n-1]
        