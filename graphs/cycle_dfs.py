# Detect a Cycle in an Undirected Graph using DFS

class Solution:
    def isCycle(self, V: int, adj: list[list[int]]) -> bool:
        vis = [False] * V  # Visited array to track visited nodes

        # DFS function to check for cycles
        def dfs(node, parent):
            vis[node] = True  # Mark the current node as visited

            for neighbor in adj[node]:  # Explore all neighbors
                if not vis[neighbor]:  # If neighbor is unvisited
                    if dfs(neighbor, node):  # Recur with the current node as parent
                        return True  # Cycle detected
                elif neighbor != parent:  # If neighbor is visited and not the parent
                    return True  # Cycle detected

            return False  # No cycle found in this component

        # Iterate through all nodes to handle disconnected components
        for i in range(V):
            if not vis[i]:  # If the node is unvisited
                if dfs(i, -1):  # Start DFS from this node
                    return True  # Cycle detected

        return False  # No cycle found in any component

'''
Time Complexity: O(N + 2E) + O(N), Where N = Nodes, 2E is for total degrees as we traverse all adjacent nodes. In the case of connected components of a graph, it will take another O(N) time.

Space Complexity: O(N) + O(N) ~ O(N), Space for recursive stack space and visited array.
'''