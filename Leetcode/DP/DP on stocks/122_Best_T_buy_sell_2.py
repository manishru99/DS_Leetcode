# 122. Best Time to Buy and Sell Stock II

# Recursive
# TC = O(2^n) - Since every day (n) has two states (buy or sell), this forms a recursive tree with O(2^n) complexity.
# SC = O(n)
class Solution:
    def f(self, ind: int, buy: int, prices: List[int], n: int) -> int:
        """
        Recursive function to determine maximum profit.

        Args:
        ind (int): Current index in prices list.
        buy (int): Flag indicating whether we can buy (1) or need to sell (0).
        prices (List[int]): List of stock prices.
        n (int): Total number of days.

        Returns:
        int: Maximum profit attainable.
        """

        # Base Case: If we reach the end of the price list, no transactions can be made.
        if ind == n:
            return 0
        profit = 0
        # Main condition 1: If we are allowed to buy a stock on the current day
        if buy:
            # Two choices:
            # 1. Buy the stock at current price and move to the next day (switch to sell mode)
            # 2. Skip buying and move to the next day (keep buy mode active)
            profit = max(
                -prices[ind] + self.f(ind + 1, 0, prices, n),  # Buying (Todays price will be subtracted)
                0 + self.f(ind + 1, 1, prices, n)  # Skipping 
            )
        # Main cond 2: If we are NOT allowed to buy a stock on the current day
        else:
            # If we need to sell the stock
            # Two choices:
            # 1. Sell the stock at current price and move to next day (switch to buy mode)
            # 2. Skip selling and move to next day (keep sell mode active)
            profit = max(
                prices[ind] + self.f(ind + 1, 1, prices, n),  #  (todays price will be added)
                0 + self.f(ind + 1, 0, prices, n)  # Skipping (todays price will not be added)
            )

        return profit

    def maxProfit(self, prices: List[int]) -> int:
        """
        Function to calculate maximum possible profit from stock prices.

        Args:
        prices (List[int]): List of daily stock prices.

        Returns:
        int: Maximum profit possible.
        """
        n = len(prices)  # Number of days
        return self.f(0, 1, prices, n)  # Start recursion from day 0, allowing buy transactions
    
# Memoization
'''
Time Complexity: O(N*2) 
Reason: There are N*2 states therefore at max ‘N*2’ new problems will be solved and we are running a for loop for ‘N’ times to calculate the total sum

Space Complexity: O(N*2) + O(N)
Reason: We are using a recursion stack space(O(N)) and a 2D array ( O(N*2)).

Logic:
- Base Case
- If ind == n, meaning all days are processed, return 0 (no profit possible).
- Memoization Check
- If dp[ind][buy] != -1, return the cached result to prevent recomputation.
- Recursive Profit Calculation
- If buy == 1: Choose between buying the stock (-prices[ind]) or skipping.
- If buy == 0: Choose between selling (+prices[ind]) or skipping.
- Store the maximum profit for each state in dp[ind][buy].
- maxProfit() Function
- Initializes dp as a 2D list of [-1], ensuring all states are initially undefined.
- Starts recursion from ind = 0 with buy = 1.
'''
class Solution:
    def f(self, ind, buy, prices, n, dp):
        # base
        if ind ==n:
            return 0
        if dp[ind][buy] != -1: return dp[ind][buy]
        profit = 0
        if buy:
            profit = max(-prices[ind] + self.f(ind + 1, 0, prices, n, dp), 0 + self.f(ind + 1, 1, prices, n, dp))
        else:
            profit = max( prices[ind] + self.f(ind + 1, 1, prices, n, dp), 0 + self.f(ind + 1, 0, prices, n, dp))
        dp[ind][buy] = profit # save max profit we got from either if or else
        return dp[ind][buy]
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0: return 0
        dp = [[-1 for _ in range(2)] for _ in range(n)]
        return self.f(0, 1, prices, n, dp)

# Tabulation
# TC = O(n^2) SC = O(n^2)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0: return 0
        dp = [[0 for _ in range(2)] for _ in range(n+1)] # n+1 as base cond is when we exceed the index
        # base 
        dp[n][0] = dp[n][1] = 0
        for ind in range(n - 1, -1, -1):
            for buy in range(2):
                profit = 0
                if buy:
                    profit = max( -prices[ind] + dp[ind+1][0], 
                    0 + dp[ind + 1][1] )
                else:
                    profit = max( prices[ind] + dp[ind + 1][1],
                    0 + dp[ind + 1][0] )
                dp[ind][buy] = profit
        return dp[0][1]

        