# 210. Course Schedule II
# G-19. Detect cycle in a directed

# The undirected graph logic fails for directed graphs because it only checks
# if a node has been previously visited (2:31). In a directed graph, a cycle 
# only exists if you revisit a node on the same path you are currently traversing.
# The undirected approach would incorrectly identify a cycle in cases where you 
# simply encounter a previously visited node that is not part of your current 
# directed path, but rather a node visited in a different path or branch of the graph.

# Logic: On the same path, the node has to be visited again

class Solution:
    def dfsTopo(self, node, adj, vis, pathVis, stack):
        vis[node] = True
        pathVis[node] = True

        for neigh in adj[node]:
            if not vis[neigh]:
                if self.dfsTopo(neigh, adj, vis, pathVis, stack):
                    return True  # Cycle detected
            elif pathVis[neigh]:
                return True  # Cycle detected

        pathVis[node] = False  # Backtrack
        stack.append(node)     # Post-order: add to stack after visiting all neighbors
        return False

    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # Build adjacency list
        adj = [[] for _ in range(numCourses)]
        for dest, src in prerequisites:
            adj[src].append(dest)

        vis = [False] * numCourses
        pathVis = [False] * numCourses
        stack = []

        # Perform DFS for all nodes
        for i in range(numCourses):
            if not vis[i]:
                if self.dfsTopo(i, adj, vis, pathVis, stack):
                    return []  # Cycle detected, no valid ordering

        # Reverse post-order stack to get topological sort
        return stack[::-1] 