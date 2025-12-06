# 110. Balanced Binary Tree
# Rfr Neetcode sol

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution 1
# TC = O(n^2)
# SC = O(n) n is the num of nodes
class Solution:
    # Traversal
    def getHeight(self, root):
        if not root: return 0
        lefth = self.getHeight(root.left)
        righth = self.getHeight(root.right)
        return 1 + max(lefth, righth)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        lefth = self.getHeight(root.left)
        righth = self.getHeight(root.right)

        if abs(lefth - righth) > 1: return False
        else: 
            if self.isBalanced(root.left) and self.isBalanced(root.right):
                return True
            
        '''
        # Removed redundant 'else' block
        if self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        '''
        return False
        

# Optimized
# TC = O(n)
# SC = O(h)

'''
This approach smartly combines DFS traversal with early pruning—as soon as any 
subtree is unbalanced, it bubbles up -1 to avoid unnecessary checks.
'''
class Solution:    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # A binary tree is balanced if the dfsHeight doesn't return -1
        return self.dfsHeight(root) != -1

    def dfsHeight(self, root):
        # Base case: an empty tree has height 0 and is considered balanced
        if not root:
            return 0

        # Recursively get the height of the left subtree
        lh = self.dfsHeight(root.left)
        # If left subtree is unbalanced, propagate failure upward
        if lh == -1:
            return -1

        # Recursively get the height of the right subtree
        rh = self.dfsHeight(root.right)
        # If right subtree is unbalanced, propagate failure upward
        if rh == -1:
            return -1

        # Check if current node is unbalanced (height difference > 1)
        if abs(lh - rh) > 1:
            return -1

        # If balanced, return height of current subtree
        return 1 + max(lh, rh)