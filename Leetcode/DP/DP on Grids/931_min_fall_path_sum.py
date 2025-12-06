# 931. Minimum Falling Path Sum

# Recursion 
# TC = O(3^n) - Exponential due to 3 recursive calls at each level
# SC = O(n) st space due to recursion depth equal to num of rows 
class Solution:
    def f(self, i, j, n, matrix):
        # base 1
        if j < 0 or j >= n: return int(1e9)
        # base 2
        if i == 0: return matrix[0][j]
        # straight
        s = matrix[i][j] + self.f(i-1, j, n, matrix)
        # left diagonal
        ld = matrix[i][j] + self.f(i-1, j-1, n, matrix)
        # right diag
        rd = matrix[i][j] + self.f(i-1, j+1, n, matrix)
        return min(s, min(ld, rd))

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        mini = sys.maxsize 
        for j in range(n):
            ans = self.f(n-1, j, n, matrix)
            mini = min(mini, ans)
        return mini
    
# Memoization

# TC = O(n^2) - each cell is computed once
# SC = O(n^2) for dp arr + O(n) for recursion st space
# Recursive function to find the maximum path sum starting from cell (i, j)
def getMaxUtil(i, j, m, matrix, dp):
    # Base case: If j is out of bounds, return a large negative value
    if j < 0 or j >= m:
        return -int(1e9)
    
    # Base case: If we are at the top row (i == 0), return the value in the current cell
    if i == 0:
        return matrix[0][j]
    
    # Check if the maximum path sum for this cell has already been computed
    if dp[i][j] != -1:
        return dp[i][j]
    
    # Calculate three possible moves: going up, going up-left, and going up-right
    up = matrix[i][j] + getMaxUtil(i - 1, j, m, matrix, dp)
    leftDiagonal = matrix[i][j] + getMaxUtil(i - 1, j - 1, m, matrix, dp)
    rightDiagonal = matrix[i][j] + getMaxUtil(i - 1, j + 1, m, matrix, dp)
    
    # Store the maximum of the three moves in the memoization table
    dp[i][j] = max(up, max(leftDiagonal, rightDiagonal))
    return dp[i][j]

# Function to find the maximum path sum in the matrix
def getMaxPathSum(matrix):
    n = len(matrix)  # Number of rows
    m = len(matrix[0])  # Number of columns
    dp = [[-1 for j in range(m)] for i in range(n)]  # Initialize a memoization table
    maxi = -sys.maxsize  # Initialize the maximum sum to a large negative value
    
    # Iterate through the first row and find the maximum path sum starting from each cell
    for j in range(m):
        ans = getMaxUtil(n - 1, j, m, matrix, dp)
        maxi = max(maxi, ans)
    
    return maxi  # Return the maximum path sum


# Tabulation
def getMaxPathSum(matrix):
    n = len(matrix)
    m = len(matrix[0])

    # Step 1: Initialize the dp table with the same dimensions as the matrix
    dp = [[0 for _ in range(m)] for _ in range(n)]

    # Step 2: Base case — first row of dp is same as first row of matrix
    for j in range(m):
        dp[0][j] = matrix[0][j]

    # Step 3: Fill the dp table from second row to last row
    for i in range(1, n):
        for j in range(m):
            # Possible moves with bounds checking
            up = dp[i - 1][j]
            leftDiagonal = dp[i - 1][j - 1] if j - 1 >= 0 else float('-inf')
            rightDiagonal = dp[i - 1][j + 1] if j + 1 < m else float('-inf')

            dp[i][j] = matrix[i][j] + max(up, leftDiagonal, rightDiagonal)

    # Step 4: The answer is the max in the last row
    return max(dp[n - 1])
