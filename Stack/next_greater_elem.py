
'''
TC = O(n)
The loop iterates over the array exactly once (for i in range(len(arr))), contributing O(n).

The while loop pops elements from the stack. Each element is pushed to and popped from the stack exactly once, so the overall cost of all while loops across the function is O(n).

Combining these, the function runs in O(n) time.

SC = O(n)
The stack (st) can grow up to the size of the input array in the worst case, contributing O(n).

The result array (res) is also O(n), as it stores one element for each input element.

Thus, the overall space complexity is O(n).
'''

def next_greater_element(arr):
    stack = []
    result = [-1] * len(arr)  # Initialize result with -1 (default if no greater element exists)

    # Traverse the array from right to left
    for i in range(len(arr) - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:  # Maintain a decreasing stack
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(arr[i])

    return result

def previous_smaller_element(arr):
    stack = []
    result = [-1] * len(arr)  # Initialize result with -1 (default if no smaller element exists)

    # Traverse the array from left to right
    for i in range(len(arr)):
        while stack and stack[-1] >= arr[i]:  # Maintain an increasing stack
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(arr[i])

    return result

def next_smaller_element(arr):
    stack = []
    result = [-1] * len(arr)  # Initialize result with -1 (default if no smaller element exists)

    # Traverse the array from right to left
    for i in range(len(arr) - 1, -1, -1):
        while stack and stack[-1] >= arr[i]:  # Maintain an increasing stack
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(arr[i])

    return result

def previous_greater_element(arr):
    stack = []
    result = [-1] * len(arr)  # Initialize result with -1 (default if no greater element exists)

    # Traverse the array from left to right
    for i in range(len(arr)):
        while stack and stack[-1] <= arr[i]:  # Maintain a decreasing stack
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(arr[i])

    return result

