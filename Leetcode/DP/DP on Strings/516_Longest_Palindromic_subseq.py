# 516. Longest Palindromic Subsequence

class Solution:
    def lcs(self, s, t):
        m, n = len(s), len(t)
        dp = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
        # 1st col
        for i in range(m + 1): # row will be from 0 to m
            dp[i][0] = 0
        # 1st row
        for i in range(n + 1):
            dp[0][i] = 0
        for ind1 in range(1, m + 1):
            for ind2 in range(1, n + 1):
                # match
                if s[ind1 - 1] == t[ind2 - 1]:
                    dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1] # diagonal
                # not match
                else:
                    dp[ind1][ind2] = max(dp[ind1 - 1][ind2], dp[ind1][ind2 - 1])
        return dp[m][n]

    def longestPalindromeSubseq(self, s: str) -> int:
        t = s
        s = s[::-1]
        return self.lcs(s, t)