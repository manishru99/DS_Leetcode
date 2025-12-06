# 173. Binary Search Tree Iterator

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    """
    Implements an iterator for a Binary Search Tree (BST) that returns
    elements in ascending order (in-order traversal).
    """
    def __init__(self, root: TreeNode):
        """
        Initializes the iterator.
        The stack stores TreeNodes to simulate an in-order traversal.
        """
        self.stack = []  # Use a Python list as a stack
        self._push_all(root)

    def hasNext(self) -> bool:
        """
        Returns True if there's a next smallest number, False otherwise.
        This is true if the stack is not empty.
        """
        return len(self.stack) > 0  # Check if the stack is not empty

    def next(self) -> int:
        """
        Returns the next smallest number in the BST.
        Pops the top node from the stack, pushes its right subtree's
        leftmost path onto the stack, and returns the popped node's value.
        """
        if not self.hasNext():
            raise StopIteration("No more elements in the BST.")

        tmp_node = self.stack.pop()
        self._push_all(tmp_node.right)
        return tmp_node.val

    def _push_all(self, node: TreeNode):
        """
        Helper method to push all leftmost nodes from a given node
        onto the stack. This effectively finds the next smallest element
        or prepares for the next in-order successor.
        """
        while node is not None:
            self.stack.append(node)
            node = node.left

# --- Example Usage ---
if __name__ == "__main__":
    # Construct a sample BST:
    #      7
    #     / \
    #    3   15
    #       /  \
    #      9    20
    root = TreeNode(7)
    root.left = TreeNode(3)
    root.right = TreeNode(15)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(20)

    iterator = BSTIterator(root)

    print(iterator.next())    # Output: 3
    print(iterator.next())    # Output: 7
    print(iterator.hasNext()) # Output: True
    print(iterator.next())    # Output: 9
    print(iterator.hasNext()) # Output: True
    print(iterator.next())    # Output: 15
    print(iterator.hasNext()) # Output: True
    print(iterator.next())    # Output: 20
    print(iterator.hasNext()) # Output: False

    try:
        print(iterator.next())
    except StopIteration as e:
        print(e) # Output: No more elements in the BST.