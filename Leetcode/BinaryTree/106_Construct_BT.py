# 106. Construct Binary Tree from Inorder and Postorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inMap = {}
        for idx, val in enumerate(inorder):
            inMap[val] = idx
        root = self._buildTree(postorder, 0, len(postorder)-1, inorder, 0, len(inorder)-1, inMap)
        return root
    
    def _buildTree(self, postorder, postStart, postEnd, inorder, inStart, inEnd, inMap):
        # base case
        if postStart > postEnd or inStart > inEnd:
            return None
        root = TreeNode(postorder[postEnd])
        inRoot = inMap[root.val]
        numsleft = inRoot - inStart
        # left subtree
        root.left = self._buildTree(postorder, postStart, postStart+numsleft-1, inorder, inStart, inRoot-1, inMap)
        #right subtree
        root.right = self._buildTree(postorder, postStart+numsleft, postEnd-1, inorder, inRoot+1, inEnd, inMap)
        return root
