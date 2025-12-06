# 518. Coin Change II

# Recursive
# TC -> >> O(2^n)
# SC -> >> O(n)
'''
if T == 0: return 0 This edge case is incorrect here from Coin Change 1
- If T == 0, you should return 1 because there is exactly one way to make a sum of 0—by choosing no coins.
'''
class Solution:
    def f(self, ind, T, coins):
        # Base case: Only one coin type left
        # If the target T is divisible by this coin, there's exactly one way to form it
        if ind == 0:
            return 1 if T % coins[ind] == 0 else 0

        # Option 1: Do not take the current coin
        not_take = self.f(ind - 1, T, coins)

        # Option 2: Take the current coin (if it's not larger than the target)
        # Stay at the same index since coins can be reused (unbounded knapsack)
        take = 0
        if coins[ind] <= T:
            take = self.f(ind, T - coins[ind], coins)

        # Total ways = ways by taking + ways by not taking
        return not_take + take

    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        # Start recursion from the last index with full amount
        return self.f(n - 1, amount, coins)

# Memoization
'''
Time Complexity: O(N*T)
Reason: There are N*T states therefore at max ‘N*T’ new problems will be solved.

Space Complexity: O(N*T) + O(N)
Reason: We are using a recursion stack space(O(N)) and a 2D array ( O(N*T)).

Here dp is initilized with -1, which is a common practice to indicate that a state has not been computed yet.
'''
class Solution:
    def f(self, ind, T, coins, dp):
        # base
        if ind == 0:
            return 1 if T % coins[ind] == 0 else 0
        if dp[ind][T] != -1: return dp[ind][T]
        not_take = self.f(ind - 1, T, coins, dp)
        take = 0
        if coins[ind] <= T:
            take = self.f(ind, T - coins[ind], coins, dp)
        dp[ind][T] = not_take + take
        return dp[ind][T]

    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[-1 for _ in range(amount + 1)] for _ in range(n)]
        return self.f(n - 1, amount, coins, dp)

# Tabulation

'''
Time Complexity: O(N*T)
Reason: There are two nested loops

Space Complexity: O(N*T)
Reason: We are using an external array of size ‘N*T’. Stack Space is eliminated.
'''
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0 for _ in range(amount + 1)] for _ in range(n)]
        # Base Case: If we need 0 amount, there is exactly 1 way (empty set)
        for i in range(n):
            dp[i][0] = 1
        # base
        for i in range(amount+1):
            if i % coins[0] == 0:
                dp[0][i] = 1
        for ind in range(1, n):
            for T in range(amount + 1):
                not_take = dp[ind - 1][T]
                take = 0
                if coins[ind] <= T:
                    take = dp[ind][T - coins[ind]] 
                dp[ind][T] = take + not_take
        return dp[n - 1][amount]
