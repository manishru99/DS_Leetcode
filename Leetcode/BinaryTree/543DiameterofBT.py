# 543. Diameter of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Naive solution
# every node as a potential `Curving Point` of the diameter path.
# For each node, we calculate the height of its left and right subtrees, 
# and then we can calculate the diameter as the sum of these two heights.
# TC = O(n^2)
# SC = O(n)
'''The longest path between two leaf nodes, which runs through their 
lowest common ancestor, and is measured in edges.
'''
class Solution:
    #Can globally declare the diameter (maxi) or pass it as a parameter to the function
    def __init__(self):
    # Initialize diameter to track the maximum path length
        self.diameter = 0

def calculateH(self, root):
    # Base case: an empty node has height 0
    if root is None:
        return 0

    # Recursively calculate the height of the left subtree
    lh = self.calculateH(root.left)

    # Recursively calculate the height of the right subtree
    rh = self.calculateH(root.right)

    # Update the diameter if the path through the current node is longer
    # The path length at this node is the sum of left and right subtree heights
    self.diameter = max(self.diameter, lh + rh)

    # Return the height of the current node: 1 (itself) + max height of its subtrees
    return 1 + max(lh, rh)  # return going to calculateH() in lh and rh

def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    # Start the recursive depth-first computation from the root
    self.calculateH(root)

    # After traversal, diameter will hold the length of the longest path in the tree
    return self.diameter



# Solution 2
'''We use `diameter = [0]` instead of `diameter = 0` because lists are **mutable** in Python 
and can be updated inside recursive calls. If we used an integer (`diameter = 0`), changes
made in deeper recursive levels wouldn’t persist outside the function scope — but with a 
list, we can modify `diameter[0]` from anywhere and retain the updated value across the entire recursion.
'''
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Initialize diameter as a list to allow updates inside recursive calls
        diameter = [0]
        
        # Start recursive height calculation which also updates diameter
        self.height(root, diameter)
        
        # Return the maximum diameter found
        return diameter[0]

    def height(self, root, diameter):
        # Base case: if node is None, height is 0
        if root is None:
            return 0
        
        # Recursively compute height of left and right subtrees
        lh = self.height(root.left, diameter)
        rh = self.height(root.right, diameter)
        
        # Update diameter: max of current diameter or path through current node (lh + rh)
        diameter[0] = max(diameter[0], lh + rh)
        
        # Return height of current node: 1 + max of left/right subtree heights
        return 1 + max(lh, rh)
    

'''
# Optimized solution
# TC = O(n) SC = O(n)
Java Code
class Solution {
    // Function to find the
    // diameter of a binary tree
    public int diameterOfBinaryTree(Node root) {
        // Initialize the variable to
        // store the diameter of the tree
        // Here diameter is passed by reference
        // since variables are passed by value in java
        //meaning the method receives a copy of the variable's value, not the original. 
        //Changes inside the method do not affect the original variable

        //refer primitive data types (int, char, float, etc.) are always passed by value, 
        // and objects are passed by reference (actually, a copy of the reference is passed):
        // Explanation on gpt
        

        int[] diameter = new int[1];
        diameter[0] = 0;
        // Call the height function to traverse
        // the tree and calculate diameter
        height(root, diameter);
        // Return the calculated diameter
        return diameter[0];
    }

    // Function to calculate the height of
    // the tree and update the diameter
    private int height(Node node, int[] diameter) {
        // Base case: If the node is null,
        // return 0 indicating the
        // height of an empty tree
        if (node == null) {
            return 0;
        }

        // Recursively calculate the
        // height of left and right subtrees
        int[] lh = new int[1];
        int[] rh = new int[1];
        lh[0] = height(node.left, diameter);
        rh[0] = height(node.right, diameter);

        // Update the diameter with the maximum
        // of current diameter or sum of
        // left and right heights
        diameter[0] = Math.max(diameter[0], lh[0] + rh[0]);

        // Return the height of
        // the current node's subtree
        return 1 + Math.max(lh[0], rh[0]);
    }
}
'''