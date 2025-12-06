# 678. Valid Parenthesis String

# TC = O(3^n) (worst case) as we have 3 choices for each '*' (treat as '(), ')', or empty)
# SC = O(n) (for recursion stack)
class Solution:
    def f(self, s, ind, cnt, n):
        # Edge case: If the count goes negative, return False (invalid string)
        if cnt < 0:
            return False

        # Base case: If we've processed all characters, check if the count is zero
        if ind == n:
            return cnt == 0

        # If the current character is '(', increase the count
        if s[ind] == '(':
            return self.f(s, ind + 1, cnt + 1, n)

        # If the current character is ')', decrease the count
        if s[ind] == ')':
            return self.f(s, ind + 1, cnt - 1, n)

        # If the current character is '*', three possible cases: treat as '(', ')', or empty
        return (
            self.f(s, ind + 1, cnt + 1, n) or  # Treat '*' as '('
            self.f(s, ind + 1, cnt - 1, n) or  # Treat '*' as ')'
            self.f(s, ind + 1, cnt, n)         # Treat '*' as empty
        )

    def checkValidString(self, s: str) -> bool:
        # Call helper function `f` with initial index and count
        return self.f(s, 0, 0, len(s))
    
# Solution 2
# Or we can use Memoization, tabulation or space optimization
# TC = O(n^2) for DP table
# SC = O(n^2)
def checkValidString(self, s: str) -> bool:
    # Length of the input string
    n = len(s)

    # Create a DP table (n+1 rows, 2*n+1 columns to handle all possible balances)
    dp = [[False] * (2 * n + 1) for _ in range(n + 1)]

    # Initialize the starting state: index 0 and count (balance) = 0
    dp[0][n] = True

    # Populate the DP table
    for ind in range(n):
        for cnt in range(2 * n + 1):
            # If the current state is not valid, skip
            if not dp[ind][cnt]:
                continue
            
            # If current character is '(' -> increase the count (balance)
            if s[ind] == '(' and cnt + 1 < 2 * n + 1:
                dp[ind + 1][cnt + 1] = True
            
            # If current character is ')' -> decrease the count (balance)
            elif s[ind] == ')' and cnt - 1 >= 0:
                dp[ind + 1][cnt - 1] = True
            
            # If current character is '*' -> consider all three possibilities
            elif s[ind] == '*':
                # Treat '*' as '('
                if cnt + 1 < 2 * n + 1:
                    dp[ind + 1][cnt + 1] = True
                # Treat '*' as ')'
                if cnt - 1 >= 0:
                    dp[ind + 1][cnt - 1] = True
                # Treat '*' as empty
                dp[ind + 1][cnt] = True

    # Return whether the ending state with balance = 0 is valid
    return dp[n][n]

# Solution 3
# Greedy approach
# Two pointers to track the min and max balance of parentheses

# TC = O(n)
# SC = O(1)

def checkValidString(self, s: str) -> bool:
    n = len(s)
    # `min1` and `max1` track the possible range of valid counts of open parentheses.
    # `min1`: Minimum possible open parentheses considering '*' as ')'.
    # `max1`: Maximum possible open parentheses considering '*' as '('.
    min1, max1 = 0, 0
    for i in range(n):
        # If the current character is an '(', it increases both min1 and max1
        # since '(' adds an open parenthesis.
        if s[i] == '(':
            min1 += 1
            max1 += 1

        # If the current character is a ')', it decreases both min1 and max1
        # since ')' closes an open parenthesis.
        elif s[i] == ')':
            min1 -= 1
            max1 -= 1

        # If the current character is '*', it can behave in three ways:
        # 1. As an '(', increasing max1.
        # 2. As a ')', decreasing min1.
        # 3. As an empty string, leaving min1 and max1 unchanged.
        else:
            min1 -= 1   # Treat '*' as ')'.
            max1 += 1   # Treat '*' as '('.

        # If at any point `min1` becomes negative, reset it to 0 because
        # a negative count means we've consumed more ')' than possible '(',
        # which is invalid but can still recover with a later '*'.
        # That means we can treat '*' as an open parenthesis to balance it out.
        if min1 < 0:
            min1 = 0

        # If `max1` becomes negative, it means we have more ')' than '('
        # even with all '*' considered as '('. This means the string is invalid.
        if max1 < 0:
            return False

    # After processing all characters, `min1` should be 0 for the string
    # to be valid. If `min1 != 0`, it means there are unmatched '(' left.
    return (min1 == 0)