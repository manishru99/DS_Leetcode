# 98. Validate Binary Search Tree
'''
- Time Complexity: O(N) (visits each node once).
- Space Complexity:
- O(log₂ N) for a balanced BST.
- O(N) for a skewed BST due to recursive call stack growth.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTHelper(root, float('-inf'), float('inf'))
    
    def isValidBSTHelper(self, root, minVal, maxVal):
        if not root: return True
        # If out of range return false
        if root.val >= maxVal or root.val <= minVal:
            return False
        return self.isValidBSTHelper(root.left, minVal, root.val) and self.isValidBSTHelper(root.right, root.val, maxVal)

# Note: Here for python we have kept the function/method name different as python doesn't support method overloading like java.
'''
Why does Java allow method overloading?
- Java is a statically typed language, meaning method signatures (name + parameter types/count) are resolved at compile time.
- When Java compiles your code, it checks the number and type of arguments to determine which method to call.
Why doesn't Python support it?
- Python is dynamically typed, meaning functions are interpreted at runtime, not compiled beforehand.
- In Python, function definitions are simply reassigned in memory, so defining multiple functions with the same name just overwrites the previous one.
While you can't have true method overloading, Python provides some alternatives:
- Using Default Arguments
- Using Variable-Length Arguments
- Using Keyword Arguments
'''