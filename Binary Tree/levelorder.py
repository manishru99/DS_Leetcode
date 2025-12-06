from collections import deque
class Node:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root):
        #Store levels
        ans = []
        if not root:
            return ans #return empty list
        #Queue to store nodes for level order traversal
        q = deque()
        #Enqueue root node first
        q.append(root)

        while q:
            size = len(q)
            #List to store nodes at current level
            nodes_level = []
            for i in range(size):
                #Get the front node in the queue
                node = q.popleft()
                # Store the node value
                # in the current level list
                nodes_level.append(node.val)

                # Enqueue the child nodes if they exist
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            # Store the current level
            # in the answer list
            ans.append(nodes_level)
        return ans

# For finding the total number of levels in binary tree: len(ans)
        



def printList(lst):
# Iterate through the
# list and print each element
    for num in lst:
        print(num, end=" ")
    print()

# Main function
if __name__ == "__main__":
    # Creating a sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # Create an instance
    # of the Solution class
    solution = Solution()
    # Perform level-order traversal
    result = solution.levelOrder(root)

    print("Level Order Traversal of Tree:")

    # Printing the level order traversal result
    for level in result:
        printList(level)

#TC = O(n)
#SC = O(n)