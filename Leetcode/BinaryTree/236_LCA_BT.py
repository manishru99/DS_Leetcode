# 236. Lowest Common Ancestor of a Binary Tree

# Brute force
# TC = O(2n) SC = O(2n)
# TC for 2 traversals and SC for 2 lists
class Solution:
    def find_path(self, root, target, path):
        if not root:
            return False
        path.append(root)
        if root == target:
            return True
        if (self.find_path(root.left, target, path)) or (self.find_path(root.right, target, path)):
            return True
        path.pop()
        return False

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        path_p = []
        path_q = []
        if not self.find_path(root, p, path_p) or not self.find_path(root, q, path_q):
            return None
        i = 0
        while i < len(path_p) and i < len(path_q) and path_p[i] == path_q[i]:
            i += 1
        return path_p[i - 1]
'''
Why path.pop() is used in find_path
The path list is meant to store the current traversal path from the root to the target node. As we recursively explore the tree:
- We append the current node to path when we visit it.
- If we successfully find the target node in a subtree, we keep the path as-is.
- But if we don’t find the target in either subtree, we must backtrack — meaning we remove the current node from the path using path.pop().
This ensures that the path list only contains nodes that are actually part of the path to the target.
'''

# Optimized (Rfr striver sol)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # base case
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # result 
        # 3 conditions
        # 1. Null from left but one of the LCA nodes from right
        if not left:
            return right
        # 2. Null from right but one of the LCA nodes from left
        elif not right:
            return left
        # both left and right are not null, we found our LCA result
        else:
            return root
        
'''
- Time Complexity: O(N) 
- You traverse each node once in the worst case.

- Space Complexity:
- O(log₂ N) for a balanced binary tree.
- O(N) for a skewed binary tree (due to recursion depth).
- No need to store paths or extra data structures.

eg Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 6, q = 4
Output: 5
Explanation: The LCA of nodes 6 and 4 is 5.
'''