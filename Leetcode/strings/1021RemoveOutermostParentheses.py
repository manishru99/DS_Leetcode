# 1021. Remove Outermost Parentheses

# TC = O(n) SC = O(n)
def removeOuterParentheses(s: str) -> str:
    result = []  # To store the final result
    balance = 0  # To track the balance of parentheses
    start = 0  # To mark the start of a primitive string

    for i, char in enumerate(s):
        # Update the balance
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1

        # When balance becomes 0, we found a primitive string
        if balance == 0:
            # Add the substring excluding the outermost parentheses
            result.append(s[start + 1:i])
            # Update the start to the next position
            start = i + 1

    # Join all parts to form the final result
    return ''.join(result)

# Example Usage
s = "(()())(())(()(()))"
print(removeOuterParentheses(s))  # Output: "()()()()(())"