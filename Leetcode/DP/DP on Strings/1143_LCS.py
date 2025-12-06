# 1143. Longest Common Subsequence

# Recursion
# TC = O(2^m * 2^n) = O(2^(m+n)) m is len(s1), n is len(s2)
# SC = O(m + n) for recursion stack space
class Solution:
    def f(self, ind1, ind2, s1, s2):
        # base
        if ind1 < 0 or ind2 < 0:
            return 0
        # match
        if s1[ind1] == s2[ind2]:
            return 1 + self.f(ind1 - 1, ind2 - 1, s1, s2)
        # not match
        return max(self.f(ind1 - 1, ind2, s1, s2), self.f(ind1, ind2 - 1, s1, s2))

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        return self.f(m - 1, n - 1, text1, text2)
    
# Memoization 
'''
Time Complexity: O(N*M)
Reason: There are N*M states therefore at max ‘N*M’ new problems will be solved.
Space Complexity: O(N*M) + O(N+M)
Reason: We are using an auxiliary recursion stack space(O(N+M)) (see the recursive tree, 
in the worst case, we will go till N+M calls at a time) and a 2D array ( O(N*M)).
'''
class Solution:
    def f(self, ind1, ind2, s1, s2, dp):
        # base
        if ind1 < 0 or ind2 < 0:
            return 0
        if dp[ind1][ind2] != -1: return dp[ind1][ind2]
        # match
        if s1[ind1] == s2[ind2]:
            return 1 + self.f(ind1 - 1, ind2 - 1, s1, s2, dp)
        # not match
        else:
            dp[ind1][ind2] = max(self.f(ind1 - 1, ind2, s1, s2, dp), self.f(ind1, ind2 - 1, s1, s2, dp))
        return dp[ind1][ind2]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return self.f(m - 1, n - 1, text1, text2, dp)
    
# Tabulation
# TC = O(m*n)
# SC = O(m*n)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]

        for i in range(m+1):
            dp[i][0] = 0
        for j in range(n+1):
            dp[0][j] = 0

        for ind1 in range(1, m+1):
            for ind2 in range(1, n+1):
                # match
                if text1[ind1 - 1] == text2[ind2 - 1]:
                    dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1]
                # not match
                else:
                    dp[ind1][ind2] = max(dp[ind1 - 1][ind2], dp[ind1][ind2 - 1])
        return dp[m][n]