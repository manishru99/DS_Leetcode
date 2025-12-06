# 701 Insert into a BST

# TC = O(log2 n) for a balanced BST and O(n) for a skewed BST
# SC = O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        curr = root
        while True:
            # curr root val <= val 
            # val goes to right
            if curr.val <= val:
                # make right child as curr if exists
                if curr.right: curr = curr.right
                # place val as right child
                # we are placing it on leaf as per the logic
                else:
                    curr.right = TreeNode(val)
                    break
            # curr root val > val 
            # val goes to left
            else:
                #  make left child as curr if exists
                if curr.left: curr = curr.left
                # place val as left child
                #  we are placing it on leaf as per the logic
                else:
                    curr.left = TreeNode(val)
                    break
        return root
