# 235. Lowest Common Ancestor of a Binary Search Tree

'''- Time Complexity:
- O(log₂ N) for a balanced BST.
- O(N) for a skewed BST.
- Space Complexity:
- O(log₂ N) for a balanced BST.
- O(N) for a skewed BST (due to recursive call depth).
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursive approach
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return
        curr = root.val
        # p and q lie to the right of current root
        # GO on right side for recursive calls
        if curr < p.val and curr < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        # p and q lie to the left of current root
        if curr > p.val and curr > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # If we cannot determine 
        # ie the path splits
        # that is the LCA
        return root
    
# Iterative approach
'''
- Time Complexity: O(log₂ N) for a balanced BST, O(N) for a skewed BST.
- Space Complexity: O(1) (no recursion stack)
- Note: The iterative approach is more space-efficient than the recursive one, especially for large trees.
'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            curr = root.val
            # Both nodes are greater, move right
            if curr < p.val and curr < q.val:
                root = root.right
            # Both nodes are smaller, move left
            elif curr > p.val and curr > q.val:
                root = root.left
            # If path splits, found the LCA
            else:
                return root
        return None  # Edge case if root is None