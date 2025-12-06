# 101. Symmetric Tree

'''
TC = O(n)
- Each node is visited once.
- n is the total number of nodes in the tree.
SC = O(n)
- O(h) for recursion stack, where h is the height of the tree.
- In the worst case (skewed tree), h ≈ n, so O(n).
- In the best case (balanced tree), h ≈ log n.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Helper function to check if two trees are mirror images
        def isMirror(t1, t2):
            # If both nodes are None, they are symmetric
            if not t1 and not t2:
                return True
            # If only one is None, symmetry breaks
            if not t1 or not t2:
                return False
            # Check current node values and recurse on mirrored children
            return (
                t1.val == t2.val and
                isMirror(t1.left, t2.right) and
                isMirror(t1.right, t2.left)
            )
        
        # A tree is symmetric if its left and right subtrees are mirrors
        return isMirror(root.left, root.right) if root else True