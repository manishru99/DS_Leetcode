'''
Recursion - Try all possible ways to reach the detination
Backtracking - Try all possible ways to reach the destination and backtrack if the current way is not possible

DP Steps:
Memoization:
1. define dp arr of size n+1
2. Before returning add it up to the dp array and return the last elem of the dp array ie. dp[n]
3. Whenever you see a recursion check if it is previuosly calculated or not. If yes, return it. 
If not, calculate it and store it in the dp array.

IMPORTANT:

Trick to write recurrence relation:
1. Try to represent the problem in terms of indexes. 
For example, in the case of the Fibonacci sequence, the problem can be represented 
as fib(n) = fib(n-1) + fib(n-2). 
Here, n is the index of the Fibonacci sequence.
2. Do all possible stuff on that index according to the problem statement.
3. a. Sum of all stuffs (If the question states: Count all ways )
   b. Maximum of all stuffs (If the question states: Find maximum of all stuffs)
   c. Similarly for minimum, product, etc.

Extra Points:
4. If the problem can be divided into subproblems, then it is a DP problem.
5. If the problem can be solved by solving its subproblems just once, then it is a DP problem.
6. If the problem has overlapping subproblems, then it is a DP problem.
7. If the problem has optimal substructure, then it is a DP problem.
8. If the problem has both overlapping subproblems and optimal substructure, then it is a DP problem.

9. If the problem has only optimal substructure, then it is a greedy problem.
13. If the problem has neither overlapping subproblems nor optimal substructure, then it is a greedy problem.

10. If the problem has only overlapping subproblems, then it is a divide and conquer problem.
12. If the problem has only optimal substructure, then it is a divide and conquer problem.

11. If the problem has neither overlapping subproblems nor optimal substructure, then it is a brute force problem.
'''






# 70. Climbing Stairs

# Recursive
# TC = O(2^n)
# SC = O(n) - This is due to the maximum recursion depth: the function stack will grow up to n levels deep before unwinding.
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0: return 1
        # edge case when n=1
        if n == 1: return 1
        #1 step
        #left = self.climbStairs( n-1)
        # 2 steps
        #right = self.climbStairs( n-2)
        # total
        return self.climbStairs(n-1) + self.climbStairs( n-2)

#Memoization TC = O(n) SC = O(2n)
class Solution:
    def f(self, n, dp):
        if n == 0: return 1
        if n == 1: return 1
        if dp[n] != -1: return dp[n]
        dp[n] = self.f(n - 1, dp) + self.f(n - 2, dp)
        return dp[n]

    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n + 1)
        return self.f(n, dp)
       
# Tabulation bottom-up DP
class Solution:
    def climbStairs(self, n: int) -> int:
        # TC = O(n) SC = O(n)
        # edge case (optional) when n=1 and 0
        #if n <= 1: return 1
        dp = [0] * (n+1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
    
# Space optimized
class Solution:
    def climbStairs(self, n: int) -> int:
        prev2, prev = 1, 1
        for i in range(2, n+1):
            cur_i = prev2 + prev
            prev2 = prev
            prev = cur_i
        return prev
    