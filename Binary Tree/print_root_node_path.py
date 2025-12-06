# Striver L26. Print Root to Node Path in Binary Tree
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def getPath(root, arr, x):
        # Base case
        if root is None:
            return False
        # Store this node in arr
        arr.append(root.data)
        # If this node is the target node, return True
        if root.data == x:
            return True
        # Check if the target node is present in the left or right subtree
        if (getPath(root.left, arr, x)) or (getPath(root.right, arr, x)):
            return True
        # If not present in either subtree, remove this node from arr and return False
        # # This is important to backtrack
        arr.pop()
        return False

    def printPath(root, x):
        arr = []
        if not getPath(root, arr, x):
            print("No path exists")
            return
        # Print the path
        print(" -> ".join(map(str, arr)))
        '''
        for i in range(len(arr)):
            print(arr[i], end = " ")
            print()
        '''

# Example usage
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Constructing the binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)
root.left.left.right = Node(7)
root.right.left = Node(8)



'''
- Time Complexity: O(N) (each node is visited once).
- Space Complexity:
- O(N) (worst case, storing path in arr + recursion).
- O(log₂ N) for a balanced tree (optimized recursion depth).
'''