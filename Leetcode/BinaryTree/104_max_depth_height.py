# 104. Maximum Depth of Binary Tree
# Height of a Binary Tree

# With DFS (for explanation/logic rfr Neetcode)
'''
TC = O(n) n is the num of nodes as each node of the binary tree is visited exactly once
SC = O(h) h is the height of the tree. In the case of a skewed tree, the height can be n
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            left_h = self.maxDepth(root.left)
            right_h = self.maxDepth(root.right)
            return 1 + max(left_h, right_h)




# With BFS

# The total levels is the height
from collections import deque
def maxDepth(root):
    q = deque()
    if root:
        q.append(root)

    level = 0 # level starts with 0
    while q:
        for _ in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level += 1
    return level
