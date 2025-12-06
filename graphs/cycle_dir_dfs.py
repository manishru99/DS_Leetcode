# G-19. Detect cycle in a directed graph using DFS
# Rfr LC 210: Course Schedule 2

from collections import defaultdict

class Solution:
    def dfsCheck(self, node, adj, vis, pathVis):
        vis[node] = True # Mark node as visited
        pathVis[node] = True # Track the node in the current path
        # Traverse all adj nodes
        for neigh in adj[node]:
            if not vis[neigh]: # If unvisited, recursively check for cycles
                if self.dfsCheck(neigh, adj, vis, pathVis):
                    return True
            elif pathVis[neigh]: # If visited in current path, cycle detected
                return True
        pathVis[node] = False # Backtrack: Remove node from current path tracking
        return False

    def isCyclic(self, V, adj):
        vis = [False] * V # visited arr
        pathVis = [False] * V # path vis arr

        # for connected components
        # Check all components of the graph
        for i in range(V):
            if not vis[i]:
                if self.dfsCheck(i, adj, vis, pathVis):
                    return True # cycle found
        return False # No cycle found

'''
Time and Space Complexity
- Time Complexity: O(V + E), since DFS visits each node and edge once.
- Space Complexity: O(V + E), due to adjacency list storage and recursion stack.

'''
# Driver Code
if __name__ == "__main__":
    V = 11
    adj = defaultdict(list)

    # Creating adjacency list representation of the graph
    adj[1].append(2)
    adj[2].append(3)
    adj[3].append(4)
    adj[3].append(7)
    adj[4].append(5)
    adj[5].append(6)
    adj[7].append(5)
    adj[8].append(9)
    adj[9].append(10)
    adj[10].append(8)

    solution = Solution()
    ans = solution.isCyclic(V, adj)

    print("True" if ans else "False")
