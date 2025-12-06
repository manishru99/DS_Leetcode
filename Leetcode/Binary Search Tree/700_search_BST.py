# 700. Search in a Binary Search Tree

# TC
# the worst-case time complexity is O(N), and the best-case complexity (for a balanced BST) is O(log N).
# SC = O(1)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root and root.val != val:
            if val < root:
                root = root.left
            else:
                root = root.right
            # Combined 2 lines into 1
            #root = root.left if val < root.val else root.right
        return root


''' IMPORTANT
Why is the time complexity O(log₂ N) for a balanced BST?
- Binary Search Property – In a BST, each node's left subtree contains values smaller than the node, and the right subtree contains values greater than the node. This structure enables efficient searching.
- Halving the Search Space – Every step in the search process eliminates half of the remaining elements, similar to binary search.
- Balanced BST Height – The height of a balanced BST (like AVL or Red-Black trees) is O(log₂ N) because nodes are distributed evenly.
- Example – If we have N = 1,000,000 nodes, in the worst case, we traverse log₂(1,000,000) ≈ 20 nodes, making search highly efficient.

Why is the time complexity O(N) for a skewed BST?
- Degenerate Case – A skewed BST is essentially a linked list. If all nodes are inserted in ascending or descending order, there are no left/right splits—only a chain of nodes.
- Linear Search Behavior – Searching follows a linear traversal from root to leaf, meaning the worst-case search requires visiting N nodes.
- Example – If N = 1,000,000, the worst-case search traverses all 1,000,000 nodes, making it much slower than a balanced BST.

'''