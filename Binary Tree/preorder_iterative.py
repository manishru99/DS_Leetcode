#Preorder: root -> left -> right

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
class Solution:
    def preorder(self, root):
        #List to store preorder traversal result
        preorder = []
        if root is None:
            return preorder
        #stack to store nodes during traversal
        st = []
        #Push root node
        st.append(root)

        #Perform iterative preorder traversal
        while st:
            # Get the current node
            # from the top of the stack
            root = st.pop()
            #Add the node’s value to the preorder traversal result.
            preorder.append(root.val)

            # Push the right child onto the stack if exists
            if root.right:
                st.append(root.right)
            # Push the left child onto the stack if exists
            if root.left:
                st.append(root.left)
        return preorder
        

# Creating a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Initializing the Solution class
sol = Solution()

# Getting the preorder traversal
result = sol.preorder(root)

# Displaying the preorder traversal result
print("Preorder Traversal:", end=" ")
for val in result:
    print(val, end=" ")
print()

#TC = O(n)
#SC = O(n)