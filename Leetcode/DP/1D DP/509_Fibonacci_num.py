# 509. Fibonacci Number

#Solution 1:
# Recursion
# TC = O(2^n) SC = O(n)
'''
def fib(self, n: int) -> int:
    # solution 1
    #base
    if n <= 1:
        return n
    return self.fib(n-1) + self.fib(n-2)'
'''

# Solution 2
# Memoization approach (top-down approach)
# TC = O(n) SC = O(2n) = O(n)
# space is required for memo list and recursion stack
# For the edge case:
# [dp[0], dp[1]] assumes n+1 >= 2
# if n=0, the line dp[1] will result in an IndexError because dp[1]
# does not exist (list will only have one element dp[0])
'''
class Solution:
    def fib_until(self, n: int, dp) -> int:
        #base
        if n <= 1:
            return n
        # check dp list for previously calculated Fibonacci number
        if dp[n] != -1:
            return dp[n]
        # Recursive case: calculate Fibonacci number and store it in dp
        dp[n] = self.fib_until(n-1, dp) + self.fib_until(n-2, dp)
        return dp[n] 
    
    def fib(self, n: int) -> int:
        dp = [-1] * (n+1)
        return self.fib_until(n, dp)
'''

# Solution 3
# Tabulation (bottom-up approach)
# TC = O(n) SC = O(n)
# Here we are not using an external stack space
'''
def fib(self, n: int) -> int:
    # Edge case for n = 0 - Avoiding unnecessary array allocation:
    # If n == 0, the function can immediately return 0, skipping the creation of dp = [-1] * (n+1). While this isn't a major optimization, it prevents an unnecessary allocation when n = 0.

    if n == 0:
        return 0
    # Tabulation (bottom up)
    dp = [-1] * (n+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
'''

# Solution 4
# Optimized tabulation
# TC = O(n) SC = O(1)
# Here we are not using an external stack space

def fib( n: int) -> int:
    # Edge case for n = 0
    if n == 0:
        return 0
    # Tabulation (bottom up)
    a, b = 0, 1
    for i in range(2, n+1):
        a, b = b, a+b
    return b

n = 5
print(fib(n))