# 309. Best Time to Buy and Sell Stock with Cooldown

# Recursive
class Solution:
    def f(self, ind, buy, prices, n):
        # base
        if ind >= n: return 0
        profit = 0
        if buy:
            profit = max( -prices[ind] + self.f(ind + 1, 0, prices, n),
            0 + self.f(ind + 1, 1, prices, n) )
        else:
            profit = max( prices[ind] + self.f(ind + 2, 1, prices, n), # skip 1 day
            0 + self.f(ind + 1, 0, prices, n) )
        return profit

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        return self.f(0, 1, prices, n)

# Memoization
class Solution:
    def f(self, ind, buy, prices, n, dp):
        # base
        if ind >= n: return 0
        if dp[ind][buy] != -1: return dp[ind][buy]
        profit = 0
        if buy:
            profit = max( -prices[ind] + self.f(ind + 1, 0, prices, n, dp),
            0 + self.f(ind + 1, 1, prices, n, dp) )
        else:
            profit = max( prices[ind] + self.f(ind + 2, 1, prices, n, dp),
            0 + self.f(ind + 1, 0, prices, n, dp) )
        dp[ind][buy] = profit
        return profit

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1 for _ in range(2)] for _ in range(n)]
        return self.f(0, 1, prices, n, dp)

# Tabulation
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(n + 2)]
        profit = 0
        for ind in range(n - 1, -1, -1):
            for buy in range(2):
                if buy:
                    profit = max( -prices[ind] + dp[ind+1][0], 0 + dp[ind+1][1])
                else:
                    profit = max( prices[ind] + dp[ind+2][1], 0 + dp[ind + 1][0])
                dp[ind][buy] = profit
        return dp[0][1]