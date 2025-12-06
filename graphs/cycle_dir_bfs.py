# G-23. Detect a Cycle in Directed Graph | Topological Sort | Kahn's Algorithm | BFS
# Logic: # This sort is applicable on DAG only
'''Core Idea: Topological Sort via Indegree
- Indegree tracks how many incoming edges each node has.
- Nodes with 0 indegree can be processed first (no dependencies).
- As nodes are processed, reduce the indegree of their neighbors.
- If a neighbor's indegree becomes 0, add it to the queue.

Cycle Detection Logic
- If all nodes are processed (count == V) → no cycle.
- If some nodes remain unprocessed (count < V) → cycle exists (due to unresolved dependencies).
'''

#TC: O(V+E), Each vertex and edge is processed exactly once while calculating 
# in-degrees and during the BFS traversal.
#SC: O(V+E), We store the adjacency list, an in-degree array and a queue.
from collections import deque

class Solution:
    # Function to detect a cycle in a directed graph
    def isCyclic(self, V, adj):
        # Initialize indegree list to store incoming edge count
        indegree = [0] * V

        # Calculate indegree of each node
        for i in range(V):
            for nbr in adj[i]:
                indegree[nbr] += 1

        # Initialize queue with nodes having 0 indegree
        q = deque()
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)

        # Counter to track processed nodes
        count = 0

        # Perform BFS using Kahn's algorithm
        while q:
            # Get current node
            node = q.popleft()

            # Increment processed node count
            count += 1

            # Reduce indegree of neighbors
            for nbr in adj[node]:
                indegree[nbr] -= 1

                # If indegree becomes 0, add to queue
                if indegree[nbr] == 0:
                    q.append(nbr)

        # Return True if cycle exists
        return count != V

# Number of vertices
V = 4

# Adjacency list representing directed graph
adj = [
    [1], [2], [3], [1]  
]

# Create Solution object
sol = Solution()

# Call isCyclic and print result
print("Graph contains a cycle" if sol.isCyclic(V, adj) else "No cycle")