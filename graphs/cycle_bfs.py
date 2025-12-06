# Detect Cycle in an Undirected Graph (using BFS)

from collections import deque

class Solution:
    def isCycle(self, V: int, adj: list[list[int]]) -> bool:
        vis = [False] * V  # Visited array to track visited nodes

        # BFS function to check for cycles
        def bfs(start):
            queue = deque([(start, -1)])  # Initialize queue with (current node, parent node)
            vis[start] = True  # Mark the starting node as visited

            while queue:
                node, parent = queue.popleft()  # Get the front node and its parent

                for neighbor in adj[node]:  # Explore all neighbors
                    if not vis[neighbor]:  # If neighbor is unvisited
                        vis[neighbor] = True  # Mark it as visited
                        queue.append((neighbor, node))  # Add to queue with current node as parent
                    elif neighbor != parent:  # If neighbor is visited and not the parent
                        return True  # Cycle detected

            return False  # No cycle found in this component

        # Iterate through all nodes to handle disconnected components
        for i in range(V):
            if not vis[i]:  # If the node is unvisited
                if bfs(i):  # Start BFS from this node
                    return True  # Cycle detected

        return False  # No cycle found in any component
    

'''
- Time Complexity: O(N + 2E) + O(N), 
Where N = Nodes, 2E is for total degrees as we traverse all adjacent nodes. 
In the case of connected components of a graph, it will take another O(N) time.

Space Complexity: O(N) + O(N) ~ O(N), 
Space for queue data structure and visited array.


deque([(m,n)]) creates a deque where the initial and only element is the tuple (m, n). 
Why the list? The deque constructor expects an iterable containing the items you want to put 
into the deque. If you were to use deque((m, n)), it would interpret m and n as individual 
elements, and initialize the deque with two elements, m and n, instead of one tuple (m, n). 
By wrapping the tuple in a list [(m, n)], you provide an iterable with the single desired 
tuple element to the deque constructor
'''
