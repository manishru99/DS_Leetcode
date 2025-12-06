# 115. Distinct Subsequences

# Recursion
# TC = O(2^(n + m)) for s1 2^n and 2^m for s2
# SC = O(n + m)
class Solution:
    def f(self, i, j, s, t):
        # base 1
        if j < 0: return 1
        # base 2
        if i < 0: return 0
        if s[i] == t[j]:
            # if characters match, we can either include this character in the subsequence or not
            # include: f(i - 1, j - 1, s, t)
            # not include: f(i - 1, j, s, t)
            # we can also skip the current character in s
            # and still find the subsequence in the remaining characters
            # so we add the two results together
            return self.f(i - 1, j - 1, s, t) + self.f(i - 1, j, s, t)
        else:
            # if characters do not match, we can only skip the current character in s
            # and still find the subsequence in the remaining characters
            return self.f(i - 1, j, s, t)

    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        return self.f(n - 1, m - 1, s, t)

# Memoization
# TC = O(n*m)
# SC = O(n*m) + O(n + m)
class Solution:
    def f(self, i, j, s, t, dp):
        # base 1
        if j < 0: return 1
        # base 2
        if i < 0: return 0
        if dp[i][j] != -1: return dp[i][j]
        if s[i] == t[j]:
            dp[i][j] = self.f(i - 1, j - 1, s, t, dp) + self.f(i - 1, j, s, t, dp)
        else:
            dp[i][j] = self.f(i - 1, j, s, t, dp)
        return dp[i][j]

    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        dp = [[-1 for _ in range(m)] for _ in range(n)]
        return self.f(n - 1, m - 1, s, t, dp)
    
# tabulation
# TC = O(n*m)
# SC = O(n*m)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        # Base case: There is exactly one subsequence of an empty string s2 in s1
        for i in range(n + 1):
            dp[i][0] = 1
        # Initialize dp[0][i] to 0 for i > 0 since an empty s1 cannot have a non-empty subsequence of s2
        # s1 is row, s2 is column
        # 1st row is empty string s1, 1st column is empty string s2
        # here i will start from 1 to m else it will rewrite the previous for loops 0 column (where [0,0] is 1)
        for i in range(1, m + 1):
            dp[0][i] = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n][m]
        