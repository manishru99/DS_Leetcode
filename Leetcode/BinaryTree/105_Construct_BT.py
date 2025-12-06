# 105. Construct Binary Tree from Preorder and Inorder Traversal
                    
# Rfr striver sol

# TC = O(n)
# SC = O(n) + O(n)
# n for hashmap and n in the worst case SC for a skewed tree

# TreeNode class definition
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # Create a map to store indices of elements in the inorder traversal
        # inMap = {val: idx for idx, val in enumerate(inorder)}

        # Use simpler version other than dict comprehension
        inMap = {}  
        for idx, val in enumerate(inorder):  
            inMap[val] = idx  
            # Assigns the value (val) as the key in inMap (hashmap) and sets its index (idx) as the value.

        
        # Call the private helper function to recursively build the tree
        root = self._buildTree(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1, inMap)
        
        return root

    def _buildTree(self, preorder, preStart, preEnd, inorder, inStart, inEnd, inMap):
        # Base case: If the start indices exceed the end indices, return None
        if preStart > preEnd or inStart > inEnd:
            return None

        # Create a new TreeNode with value at the current preorder index
        root = TreeNode(preorder[preStart])

        # Find the index of the current root value in the inorder traversal
        inRoot = inMap[root.val]  # as the index is the val by our logic and the val is made as the index

        # Calculate the number of elements in the left subtree
        numsLeft = inRoot - inStart

        # Recursively build the left subtree
        root.left = self._buildTree(preorder, preStart + 1, preStart + numsLeft,
                                    inorder, inStart, inRoot - 1, inMap)

        # Recursively build the right subtree
        root.right = self._buildTree(preorder, preStart + numsLeft + 1, preEnd,
                                     inorder, inRoot + 1, inEnd, inMap)

        # Return the current root node
        return root

# Function to print the inorder traversal of a tree
def printInorder(root):
    if not root:
        return
    printInorder(root.left)
    print(root.val, end=" ")
    printInorder(root.right)

# Function to print the given list
def printList(lst):
    for val in lst:
        print(val, end=" ")
    print()

# Main function
if __name__ == "__main__":
    inorder = [9, 3, 15, 20, 7]
    preorder = [3, 9, 20, 15, 7]
    
    print("Inorder List: ", end="")
    printList(inorder)
    
    print("Preorder List: ", end="")
    printList(preorder)
    
    sol = Solution()

    root = sol.buildTree(preorder, inorder)
    
    print("Inorder of Unique Binary Tree Created:")
    printInorder(root)
    print()
                           
                        
'''
Time Complexity
- The algorithm recursively builds the binary tree by iterating over the preorder list and using a hash map lookup (inMap) to find indices in the inorder list.
- Each node is processed once, and finding the root index in inMap takes O(1) time.
- The function splits the lists N times, leading to an overall O(N) time complexity.
Space Complexity
- Hash map (inMap) stores N elements, taking O(N) space.
- Recursion depth: In the worst case (skewed tree), recursion goes O(N) deep, leading to O(N) space usage.
- In a balanced tree, recursion depth is O(log₂ N).
- Total space complexity:
- O(N) in the worst case (due to recursion + hash map).
- O(log₂ N) + O(N) ≈ O(N) in a balanced tree.

'''