# 22. Generate Parentheses

# Brute
'''
TC = O(2^(2n) * 2n) = O(n * 4^n)
- The function generates all possible strings of length 2n composed of '(' and ')'.
- There are exactly 2<sup>2n</sup> such combinations.
- Each complete string is then checked for validity using the valid() function, which runs in O(2n) time in the worst case.
SC = O(2n)
'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def valid(s: str):
            # Check if a given parentheses string is valid
            open = 0
            for c in s:
                # Increment open count for '(' and decrement for ')'
                open += 1 if c == '(' else -1
                # If at any point open becomes negative, it means more ')' than '(' → invalid
                if open < 0:
                    return False
            # Valid only if open is zero (balanced)
            return open == 0

        def dfs(s: str):
            # Base case: if the length of the string reaches 2*n (n pairs of parentheses)
            if len(s) == n * 2:
                if valid(s):
                    res.append(s)  # Add to result if valid
                return

            # Try adding '(' and ')' recursively to build all combinations
            dfs(s + '(')
            dfs(s + ')')

        # Start the DFS with an empty string
        dfs("")
        return res
    
# Brute Optimized
# TC = O(2^2n) but - optimized DFS only explores valid paths:
# TC = O(O(4^n / √n))
# SC = O(2n)  - At most 2n characters are held in the recursive call stack at once
def generateParenthesis(self, n: int) -> List[str]:
    res = []

    def dfs(s, open, close):
        if len(s) == 2 * n:
            res.append(s)
            return

        if open < n:
            dfs(s + '(', open + 1, close)
        if close < open:
            dfs(s + ')', open, close + 1)

    dfs("", 0, 0)
    return res
'''- After each recursive call, the function returns back to the previous state to explore other paths — this is where the "backtracking" happens.
It doesn’t use explicit undo logic (like popping from a stack), but the recursive call stack handles that naturally by returning to the previous string state.
""          
├─ "("     
│  └─ "(("  
│     └─ "(()"  
│        └─ "(())" ✅
│     └─ "(()(" ❌ invalid, close > open prevented
│
└─ "()"    
   └─ "()(" ❌ invalid, open already 2, close not ready
   └─ "()()" ✅
'''


# Backtracking
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # global stack
        stack = []  # Temporary stack to build each parentheses combination
        res = []    # Final list to store all valid combinations

        def backtrack(openN, closedN):
            # Base case: when we've used all open and close parentheses
            if openN == closedN == n:
                res.append("".join(stack))  # Combine the stack into a string and add to results
                return

            # If we can still add an open parenthesis, do it
            if openN < n:
                stack.append("(")              # Choose '('
                backtrack(openN + 1, closedN)  # Explore further with one more '(' added
                stack.pop()                    # Backtrack: remove last added '('

            # If we can add a close parenthesis without breaking the balance
            if closedN < openN:
                stack.append(")")              # Choose ')'
                backtrack(openN, closedN + 1)  # Explore further with one more ')' added
                stack.pop()                    # Backtrack: remove last added ')'

        # Start backtracking with zero open and close parentheses placed
        backtrack(0, 0)
        return res
    
'''TC = O(4ⁿ / √n)- At first glance, with two choices at each step (add '(' or ')'), it seems like O(2 ^ 2n).
- But your logic prunes invalid states early, so it only generates valid parentheses.
- The number of valid combinations of n pairs of parentheses is given by the Catalan number, which grows asymptotically
SC = O(n)
- The stack used in your code holds up to 2n characters during generation.

'''