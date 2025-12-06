# 120. Triangle

# Use prompts like: Give a summary of the logic used/ logic used in short. 
# Recursion
'''
TC
- This recursive approach explores all possible paths from the top of the triangle to the bottom.
- At each level i, it calls two new recursive functions (f(i+1, j) and f(i+1, j+1)).
- The recursion depth is O(n) (since the triangle has n levels).
- Each level branches into two calls, leading to exponential growth.
- Total Complexity: O(2^n), since the recursion tree doubles at each step.
SC
- The function utilizes recursive calls, meaning stack space grows with recursion depth.
- The maximum recursion depth is O(n) (due to the triangle having n rows).
- No extra data structures are used beyond function parameters.
- Total Complexity: O(n) due to recursion stack memory.
'''
class Solution:
    def f(self, i, j, triangle, n):
        # base
        if i == n - 1: return triangle[i][j]
        d = triangle[i][j] + self.f(i+1, j, triangle, n) # down
        dg = triangle[i][j] + self.f(i+1, j+1, triangle, n) # diagonal down
        return min(d, dg)
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        return self.f(0, 0, triangle, n)
    
# Memoization
# TC = O(n^2)
# SC = O(n^2) for dp arr + O(n) for recursion stack space
class Solution:
    def f(self, i, j, triangle, n, dp):
        # base
        if i == n - 1: return triangle[i][j]
        if dp[i][j] != -1: return dp[i][j]
        d = triangle[i][j] + self.f(i+1, j, triangle, n, dp)
        dg = triangle[i][j] + self.f(i+1, j+1, triangle, n, dp)
        dp[i][j] = min(d, dg)
        return dp[i][j]
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        # dp of size n*n
        dp = [[-1] * n for _ in range(n)]
        return self.f(0, 0, triangle, n, dp)
    
# Tabulation
# TC = O(n^2)
# SC = O(n^2) for dpp arr. The stack space will be eliminated from memo sol
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        # dp of size n*n
        dp = [[-1] * n for _ in range(n)]
        for j in range(n):
            dp[n-1][j] = triangle[n-1][j]
        
        for i in range(n-2, -1, -1):
            for j in range(i, -1, -1):
                d = triangle[i][j] + dp[i+1][j]
                dg = triangle[i][j] + dp[i+1][j+1]
                dp[i][j] = min(d, dg)
        return dp[0][0]
