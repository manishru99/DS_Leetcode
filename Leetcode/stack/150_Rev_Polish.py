# 150. Evaluate Reverse Polish Notation

# TC = O(n)
# SC = O(n)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for c in tokens:
            if c == "+":
                st.append(st.pop() + st.pop())
            elif c == "-":
                a, b = st.pop(), st.pop()
                st.append(b - a)
            elif c == "*":
                st.append(st.pop() * st.pop())
            elif c == "/":
                a, b = st.pop(), st.pop()
                st.append(int(float(b) / a))
            else:
                st.append(int(c))
        return st[0]
    

# Brute
# TC = O(n^2)
# SC = O(n) slices create temporary copies
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Continue until we're left with a single final result
        while len(tokens) > 1:
            for i in range(len(tokens)): # O(n)
                # If the current token is an operator, we perform an operation
                if tokens[i] in "+-*/":
                    # Get the two operands before the operator
                    a = int(tokens[i - 2])
                    b = int(tokens[i - 1])

                    # Apply the operation based on the operator type
                    if tokens[i] == '+':
                        result = a + b
                    elif tokens[i] == '-':
                        result = a - b
                    elif tokens[i] == '*':
                        result = a * b
                    elif tokens[i] == '/':
                        # Truncate towards zero as required by LeetCode spec
                        result = int(a / b)

                    # creating a new list — slicing and concatenating
                    # O(n)
                    # Replace the operator and its two operands with the result
                    tokens = tokens[:i - 2] + [str(result)] + tokens[i + 1:]
                    
                    # Break and restart the loop since the token list has changed
                    break

        # Final result is the only item left in the tokens list
        return int(tokens[0])