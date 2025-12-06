# 297. Serialize and Deserialize Binary Tree
# Can be solved using level order, preorder

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from queue import Queue
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # Travel by level order to serialize
        if root is None: return ""
        q = deque()
        q.append(root)
        #q = deque([root])
        res = []
        while q:
            node = q.popleft() # remove from left
            if node is None:
                res.append("#")
            else:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
        return ",".join(res)


    def deserialize(self, data):
        """Decodes your encoded data to a binary tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # Edge case: if input data is empty, return None (no tree to build)
        if not data:
            return None

        # Split the serialized string by commas to get node values
        nodes = data.split(",")

        # The first value is always the root; create the root TreeNode
        root = TreeNode(int(nodes.pop(0)))

        # Initialize a queue to perform level-order construction
        q = deque([root])
        ''' The above is 1 line represent of below
        q = deque()
        q.append(root)
        '''

        # Continue until all nodes are processed
        while q:
            # Take the next node from the queue
            node = q.popleft()

            # Handle the left child if any nodes remain
            if nodes:
                left_val = nodes.pop(0)
                if left_val != "#":
                    # Create left child and append it to the queue
                    node.left = TreeNode(int(left_val))
                    q.append(node.left)

            # Handle the right child similarly
            if nodes:
                right_val = nodes.pop(0)
                if right_val != "#":
                    # Create right child and append it to the queue
                    node.right = TreeNode(int(right_val))
                    q.append(node.right)

        # Return the reconstructed binary tree's root node
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))