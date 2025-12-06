# Topological Sort
# By BFS | Kahn's Algorithm

from collections import defaultdict, deque

class Solution:
    def topoSort(self, V, adj):
        # Step 1: Compute in-degree for all nodes
        indegree = [0] * V
        for node in range(V):
            for neighbor in adj[node]:
                indegree[neighbor] += 1 # Increase in-degree for each neighbor

        # Step 2: Initialize queue with nodes having in-degree 0 (no dependencies)
        queue = deque()
        for i in range(V):
            if indegree[i] == 0:
                queue.append(i)

        # Step 3: Perform BFS-like traversal to process nodes in topological order
        topo_order = []
        while queue:
            node = queue.popleft() # Extract node with in-degree 0
            topo_order.append(node)

            # Step 4: Reduce in-degree for all adjacent nodes
            for neighbor in adj[node]:
                indegree[neighbor] -= 1 # Remove the dependency on the current node
                if indegree[neighbor] == 0: # If in-degree becomes zero, add to queue
                    queue.append(neighbor)
        # Step 5: Return the computed topological order
        return topo_order

'''
Time Complexity: O(V+E), where V = no. of nodes and E = no. of edges. This is a simple BFS algorithm.

Space Complexity: O(N) + O(N) ~ O(2N), O(N) for the indegree array, and O(N) for the queue data structure used in BFS(where N = no.of nodes).
'''
