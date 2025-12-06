# 322. Coin Change

# Recursive
# TC -> >> O(2^n) 
# SC -> >> O(n)
'''
- if T == 0: return 0 ✅ Correct
- This is valid because if T == 0, no coins are needed, so the answer should be 0.
- if ind < 0: return int(1e9) ❌ Incorrect
- When ind < 0, it means no more coins are left to consider.
- Returning int(1e9) here incorrectly assumes we should penalize non-reachable states, but it should be return int(1e9) only if T > 0.
- If T == 0 when ind < 0, we should return 0 instead of int(1e9).
'''
class Solution:
    def f(self, ind, T, coins):
        # Base case: If target amount is 0, no coins are needed
        if T == 0:
            return 0

        # Base case: If we've exhausted all coins and target is not 0, return large value (infeasible)
        if ind < 0:
            return 0 if T == 0 else int(1e9)

        # Base case: Only one coin type left
        if ind == 0:
            # If the target is divisible by this coin, return number of coins needed
            if T % coins[ind] == 0:
                return T // coins[ind]
            else:
                # Otherwise, it's not possible to form the amount with this coin
                return int(1e9)

        # Option 1: Do not take the current coin
        not_take = self.f(ind - 1, T, coins)

        # Option 2: Take the current coin (if it's not larger than the target)
        take = int(1e9)
        if coins[ind] <= T:
            # Take the coin and reduce the target, stay at same index (unlimited supply)
            take = 1 + self.f(ind, T - coins[ind], coins)

        # Return the minimum of both choices
        return min(take, not_take)

    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        # Start recursion from the last index
        res = self.f(n - 1, amount, coins)

        # If result is infeasible, return -1 as per problem statement
        return res if res != int(1e9) else -1


# Memoization
'''
Time Complexity: O(N*T)
Reason: There are N*T states therefore at max ‘N*T’ new problems will be solved.

Space Complexity: O(N*T) + O(N)
Reason: We are using a recursion stack space(O(N)) and a 2D array ( O(N*T)).
'''
class Solution:
    def f(self, ind, T, coins, dp):
        if T == 0: return 0
        if ind < 0: return int(1e9)
        # base
        if ind == 0:
            if T % coins[ind] == 0:
                return T // coins[ind]
            else:
                return 1e9
                #return -1
        if dp[ind][T] != -1: return dp[ind][T]
        not_take = 0 + self.f(ind - 1, T, coins, dp)
        take = int(1e9)
        if coins[ind] <= T:
            take = 1 + self.f(ind, T - coins[ind], coins, dp)
        dp[ind][T] = min(take, not_take)
        return dp[ind][T]

    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[-1 for _ in range(amount + 1)] for _ in range(n)]
        res = self.f(n-1, amount, coins, dp)
        return res if res != int(1e9) else -1
    

# Tabulation
'''
Time Complexity: O(N*T)

Reason: There are two nested loops

Space Complexity: O(N*T)

Reason: We are using an external array of size ‘N*T’. Stack Space is eliminated.
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[int(1e9) for _ in range(amount + 1)] for _ in range(n)]

        for i in range(n):
            dp[i][0] = 0
        for i in range(amount + 1):
            if i % coins[0] == 0:
                dp[0][i] = i // coins[0]
            else:
                dp[0][i] = int(1e9)

        for ind in range(1, n):
            for target in range(amount + 1):
                notTake = dp[ind - 1][target]  
                take = int(1e9)  
                if coins[ind] <= target:
                    take = 1 + dp[ind][target - coins[ind]]
                dp[ind][target] = min(notTake, take)
        ans = dp[n - 1][amount]
    
        if ans >= int(1e9):
            return -1
        return ans
