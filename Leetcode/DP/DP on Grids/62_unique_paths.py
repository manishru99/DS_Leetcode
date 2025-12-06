# 62. Unique Paths

# TC = O(2^(m+n)) for every ind we are exploring 2 paths
# SC = O(m+n) for recursion st (equal to the path length from 
# (m,n) to (1,1) and not exactly m+n)
# here path length is (m-1) + (n-1)
'''
Why O(2^(m+n))?
- The recursion creates a binary tree where each call branches into 
two new recursive calls (down or right).
- The depth of the recursion is approximately m + n (since each call
 moves either right or down).
- Each level of recursion doubles the number of calls, leading to an 
exponential time complexity of O(2^(m+n)).
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # start recursion from end pos
        # base 1
        # 1 based indexing
        if m == 1 and n == 1: return 1
        # base 2
        if m < 1 or n < 1: return 0
        # go left
        left = self.uniquePaths(m, n-1)
        # go above 
        above = self.uniquePaths(m-1, n)
        return left + above

# If there are overlapping subproblems we can apply memo 
# confirm with recursion tree

# Memoization
# TC = O(m*n) Reason: At max, there will be M*N calls of recursion.
# SC = O(m-1 + n-1) for recursion stack space + O(m*n) for dp arr 
class Solution:
    def f(self, m, n, dp):
        # start from end pos
        # base 1
        # 1 based indexing
        if m == 1 and n == 1: return 1
        # base 2
        if m < 1 or n < 1: return 0
        if dp[m][n] != -1: return dp[m][n]
        left = self.f(m, n-1, dp)
        # go above 
        above = self.f(m-1, n, dp)
        dp[m][n] = left + above
        return dp[m][n]

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1] * (n+1) for _ in range(m+1)] 
        return self.f(m, n, dp)

# Tabulation (bottom-up)
# ie base case and go up collecting 
# TC = O(m*n) Reason: There are two nested loops
# Sc = O(M*N) Reason: We are using an external array of size ‘M*N’.
def countWaysUtil(m, n, dp):
    # Loop through each cell in the grid
    for i in range(m):
        for j in range(n):
            # Base condition: If we are at the top-left corner, there is one way to reach it.
            if i == 0 and j == 0:
                dp[i][j] = 1
                continue          
            # Initialize variables to store the number of ways from above and from the left.
            up = 0
            left = 0
            # Check if moving up is a valid option (not out of bounds).
            if i > 0:
                up = dp[i - 1][j]
            # Check if moving left is a valid option (not out of bounds).
            if j > 0:
                left = dp[i][j - 1]
            # Calculate and store the number of ways to reach the current cell.
            dp[i][j] = up + left
    
    # The bottom-right cell (m-1, n-1) now contains the total number of ways to reach there.
    return dp[m - 1][n - 1]
def uniquePaths(self, m: int, n: int) -> int:
    dp = [[-1] * (n) for _ in range(m)] 
    return self.f(m, n, dp)

''' Mental Model for return self.f(m, n, dp) is correct and not return self.f(m-1, n-1, dp)
Think of m and n as dimensions, not indices.
If you want to fill a grid of size m × n, you need to loop from 0 to m - 1 and 0 to n - 1.
So passing m - 1 and n - 1 into f makes it fill only a (m - 1) × (n - 1) grid—not what you want.
'''