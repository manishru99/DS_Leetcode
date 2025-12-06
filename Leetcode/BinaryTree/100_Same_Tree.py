# 100 Same Tree (rfr Neetcode)

# brute-force approach 
'''check if two binary trees are the same would involve 
traversing both trees completely (e.g., using DFS or BFS), storing their structure and 
values in lists, and then comparing those lists. Here's how you could do it using preorder traversal
'''
# TC = O(3n) = O(n)
# - You visit every node exactly once in both trees.
# dfs(p) and dfs(q) each take O(n), and list comparison also takes O(n).
# SC = O(n)
class Solution:
    def dfs(self, root):
        if root is None:
            return [None] # Use None to preserve structure
        return [root.val] + self.dfs(root.left) + self.dfs(root.right)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        dfs1 = self.dfs(p)
        dfs2 = self.dfs(q)
        return dfs1 == dfs2
    
# Optimized

# TC = O(n) SC = O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        # If p and q both exists and at the same time vals at both p and q are equal then 
        # call the function recursively for respective left and right subtrees
        if p and q and p.val == q.val:
            # both the respective nodes left and right subtrees should return true
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False