# 547. Number of Provinces

from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)  # Total number of cities (nodes in the graph)
        vis = [False] * n     # Visited array to keep track of visited cities
        provinces = 0         # Counter for number of connected components (provinces)

        # Depth-First Search to mark all cities connected to 'node'
        def dfs(node):
            for neighbor in range(n):
                # Check if there's a connection and the neighbor hasn't been visited
                if isConnected[node][neighbor] == 1 and not vis[neighbor]:
                    vis[neighbor] = True  # Mark neighbor as visited
                    dfs(neighbor)         # Recursively visit its neighbors

        # Iterate over each city
        for i in range(n):
            if not vis[i]:               # If the city hasn't been visited yet
                vis[i] = True            # Mark it as visited
                provinces += 1           # This starts a new province
                dfs(i)                   # Traverse all cities in this province

        return provinces  # Total number of provinces (connected groups)
    
'''
Given below is the adj list 
isConnected = [[1,1,0],[1,1,0],[0,0,1]]

Time Complexity:
- We iterate through all cities once: O(n)
- For each unvisited city, we perform a DFS traversal:
- Each DFS traversal explores at most n nodes (in the worst case, when all cities are connected)
- Since each edge in the adjacency matrix isConnected[i][j] is checked once, the total DFS work is O(n²)
Thus, the overall time complexity is O(n²), since we traverse the n × n matrix as we search for connected components.
Space Complexity:
- Visited array: Takes O(n) space to track visited cities.
- Recursive stack (DFS calls): In the worst case (a fully connected graph), recursion depth could be O(n).
Thus, the overall space complexity is O(n), since no additional data structures (like adjacency lists) are used.

'''