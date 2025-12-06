# 572. Subtree of Another Tree

# TC = O(m * n)
# SC = O(m + n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If subRoot is None, it's trivially a subtree
        # edge case 3
        if not subRoot:
            return True
        # If root is None but subRoot isn't, subRoot can't be a subtree
        # edge case 4
        if not root:
            return False
        # Check if the trees rooted at current node are identical
        if self.sameTree(root, subRoot):
            return True
        # Recursively check left and right subtrees of root
        return (
            self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot)
        )
        
    def sameTree(self, root, subRoot):
        # If both nodes are None, they match
        # Edge case 1
        if not root and not subRoot:
            return True
        # If both nodes exist and have the same value, check their children
        if root and subRoot and root.val == subRoot.val:
            return (
                self.sameTree(root.left, subRoot.left) and
                self.sameTree(root.right, subRoot.right)
            )
        # If one is None or values don't match, trees aren't the same
        # edge case 2 -> above cases or all values match but there are extra values in the subtree wwhich don't match
        return False