# 124 BT Maximum Path Sum
    
# TC = O(n)
# SC = O(h)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findMaxPathSum(self, root, maxi):
        """
        Helper function to calculate the maximum path sum.
        This function computes the maximum path sum by exploring left and right subtrees recursively.
        
        Args:
        root (TreeNode): Current node of the binary tree.
        maxi (list): List storing the maximum path sum encountered so far.

        Returns:
        int: Maximum path sum that can be extended upwards from this node.
        """
        
        # Base case: If the node is null, return 0 (null nodes do not contribute to the path sum)
        if root is None:
            return 0

        # Recursively compute the max path sum from left and right subtrees
        # If the sum is negative, we discard it (i.e., take max(0, subtree sum))
        left_sum = max(0, self.findMaxPathSum(root.left, maxi))  # Left subtree contribution
        right_sum = max(0, self.findMaxPathSum(root.right, maxi))  # Right subtree contribution

        # Update the maximum path sum encountered so far
        # The best possible path through 'root' includes its value + left_sum + right_sum
        maxi[0] = max(maxi[0], left_sum + right_sum + root.val)

        # Return the maximum sum that can be extended upwards in the tree
        # We can extend either left or right subtree, not both.
        return root.val + max(left_sum, right_sum)

    def maxPathSum(self, root):
        """
        Computes the maximum path sum for any path in the binary tree.
        
        Args:
        root (TreeNode): Root of the binary tree.

        Returns:
        int: Maximum path sum in the tree.
        """
        
        # Initialize the maximum path sum as negative infinity (to handle cases with all negative nodes)
        maxi = [float('-inf')]
        
        # Call the helper function to compute the maximum path sum
        self.findMaxPathSum(root, maxi)
        
        # Return the maximum path sum found
        return maxi[0]
    

'''
Reason for Why do we create maxi as a list and then pass the first element of it? WHy not directly pass the variable maxi?
maxi = new_value
would only change the local copy of maxi, not the original one in maxPathSum. Python passes immutable types
 like integers by value, so the outer maxi wouldnt be updated.
'''