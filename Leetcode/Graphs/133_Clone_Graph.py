# 133. Clone Graph

'''
Step-by-Step Logic
- Base Case: If the input node is None, return None.
- DFS Traversal:
- If a node is already cloned (exists in oldToNew), return its clone.
- Otherwise:
- Create a new node with the same value.
- Store it in oldToNew.
- Recursively clone all its neighbors and attach them to the new node.
- Return the cloned node.
'''

# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else [] # adj list

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # HashMap to store mapping from original node to its clone
        oldToNew = {}

        def dfs(node):
            # If the node has already been cloned, return the cloned version
            if node in oldToNew:
                return oldToNew[node]

            # Create a new copy of the node
            copy = Node(node.val)
            
            # Store this newly created node in the hashmap
            oldToNew[node] = copy

            # Recursively clone all neighbors and add them to the cloned node's neighbor list
            # neighbor -> adj list
            for neigh in node.neighbors:
                copy.neighbors.append(dfs(neigh))

            # Return the cloned node
            return copy

        # If the input graph is empty, return None
        return dfs(node) if node else None
    
'''
Time Complexity Analysis:
- Each node in the graph is visited once during the DFS traversal.
- Since each node is processed and all its neighbors are cloned, the total work done is proportional to the number of vertices (V) and edges (E).
- Overall time complexity: O(V + E), where V is the number of nodes and E is the number of edges

Space Complexity Analysis:
- HashMap (oldToNew) stores copies of the original nodes → O(V).
- DFS recursive call stack can go up to O(V) in the worst case (for a fully connected graph).
- New graph storage (clone structure) also requires O(V + E).

'''