# 155. Min Stack

# USing 2 stacks
# TC = O(1) SC = O(n)
class MinStack:
    def __init__(self):
        # Main stack to store all elements
        self.stack = []
        # Auxiliary stack to track the minimum element at each level
        self.minstack = []

    def push(self, val: int) -> None:
        # Push the value to the main stack
        self.stack.append(val)

        # Compute the new minimum: either the incoming value or the current min
        val = min(val, self.minstack[-1] if self.minstack else val)
        # we are adding 'else val' condition bcos for the 1st push minstack[-1]
        # will give an IndexError so basically this will act as taking the val itself
        # ie comparing val with same val 

        # Push the updated minimum to the minstack
        self.minstack.append(val)

    def pop(self) -> None:
        # Remove the top element from both stacks
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        # Return the top element from the main stack
        return self.stack[-1]

    def getMin(self) -> int:
        # Return the current minimum from the minstack
        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

'''One-Stack Strategy
Each stack element stores a pair: (val, current_min_at_this_point)
'''
class MinStack:
    def __init__(self):
        # Stack stores tuples: (value, min_so_far)
        self.stack = []

    def push(self, val: int) -> None:
        min_so_far = val if not self.stack else min(val, self.stack[-1][1])
        self.stack.append((val, min_so_far))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
