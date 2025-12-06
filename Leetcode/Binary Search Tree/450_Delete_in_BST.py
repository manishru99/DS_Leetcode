# 450 Delete in a BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        # Key found at root
        if root.val == key:
            return self.helper(root)
        # key is less than root
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        # key is greater than root
        else:
            root.right = self.deleteNode(root.right, key)
        return root
    
    def helper(self, root: TreeNode) -> TreeNode:
        # left child is null
        if not root.left:
            return root.right
        # right child is null
        elif not root.right:
            return root.left
        else:
            right_child = root.right
            # last right is the one below (on right child) which we have to attach the right subtree
            last_right = self.findLastRight(root.left)
            # attach
            last_right.right = right_child  
        return root.left
    
    def findLastRight(self, root: TreeNode) -> TreeNode:
        while root.right:
            root = root.right
        return root
    

'''
Time Complexity
The function deleteNode operates recursively, and the time complexity depends on the structure of the Binary Search Tree (BST):
- Finding the Node to Delete – This takes O(log₂ N) in a balanced BST (since we traverse at most the height of the tree). In a skewed BST (linked-list-like), it takes O(N).
- Rearranging the Subtrees –
- If the node has no children or one child, deletion is O(1).
- If the node has two children, we find the rightmost node of its left subtree (handled by findLastRight). This traversal takes O(log₂ N) in a balanced tree and O(N) in a skewed tree.
Overall, the worst-case time complexity is O(N) (skewed BST), and the best-case (balanced BST) is O(log₂ N).

Space Complexity
- Recursive Calls – The recursion stack is at most O(log₂ N) deep in a balanced BST. In a skewed BST, it can go up to O(N).
- In-place Modifications – Since we don’t use additional data structures, the space complexity is O(1) (ignoring recursion overhead).
Thus, the worst-case space complexity is O(N) for an unbalanced BST due to recursion depth, and O(log₂ N) for a balanced BST.

'''