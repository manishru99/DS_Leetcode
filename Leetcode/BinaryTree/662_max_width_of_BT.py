# 662. Maximum Width of Binary Tree

# Rfr Striver code for clarity
'''
The maximum number of nodes between the leftmost and rightmost non-null nodes 
at any level of the binary tree — including null nodes in between.
Key Details
- Width is measured horizontally, level by level.
- You must account for the position of nodes, not just their count.
- Even if some nodes are missing (null), their "slots" still count toward the width.
'''
# TC = O(n) SC = O(h)
from collections import deque

# Logic: Width for a level is the number of nodes between the first node and the last 
# node in that level

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        # Edge case: If tree is empty, width is 0
        if not root:
            return 0
        
        # Queue stores tuples (node, index), where index represents the position of the node
        q = deque([(root, 0)])
        max_width = 0

        # Level-order traversal using BFS
        while q:
            size = len(q)  # Number of nodes at current level
            mmin = q[0][1]  # Minimum index at this level (used to normalize indices)
            first, last = None, None  # Track first and last node indices at the current level

            # Process all nodes at the current level
            for _ in range(size):
                node, cur_id = q.popleft()  # Efficient retrieval of node from the queue
                
                cur_id -= mmin  # Normalize index to prevent overflow in large trees
                
                # Capture first and last indices for width computation
                if first is None:
                    first = cur_id  # First node index at this level
                last = cur_id  # Update last node index

                # Add left child with calculated position
                if node.left:
                    q.append((node.left, cur_id * 2 + 1))  

                # Add right child with calculated position
                if node.right:
                    q.append((node.right, cur_id * 2 + 2))  

            # Compute the width of the current level and update max_width
            max_width = max(max_width, last - first + 1)

        return max_width