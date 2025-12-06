# 785. Is Graph Bipartite?
#- A graph is bipartite if you can color its nodes using two colors such that no two adjacent nodes share the same color.
# Logic:- Use a color array to track node colors: -1 means uncolored, 0 and 1 are the two colors.
#- For each uncolored node, perform BFS:
#- Start with color 0
#- Assign the opposite color to each neighbor
#- If any neighbor already has the same color → graph is not bipartite

# With BFS
class Solution:
    def isBipartite(self, graph):
        n = len(graph)
        color = [-1] * n  # -1 means uncolored at the start
        # color instead of vis to track 2 colors 0 and 1

        def bfs(start):
            queue = [start]
            color[start] = 0  # Start coloring with 0
            while queue:
                node = queue.pop(0)
                for neighbor in graph[node]:
                    if color[neighbor] == -1:  # If uncolored
                        color[neighbor] = 1 - color[node]  # Color with opposite color
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:  # If same color as current node
                        return False
            return True

        for i in range(n):
            if color[i] == -1:  # If uncolored, start BFS
                if not bfs(i):
                    return False

        return True
    
'''
Time Complexity Analysis
- Looping through all nodes → O(V)
- The function iterates over all nodes to check if they are uncolored and initiates BFS.
- Breadth-First Search (BFS) traversal → O(V + E)
- Each node is processed once, and each edge is checked once in the worst case.
Total Time Complexity:
[ O(V + E) ]
This is the standard time complexity for BFS-based graph traversal.

Space Complexity Analysis
- Color array (color[]) → O(V)
- Stores the color for each node (either 0 or 1).
- Queue for BFS (queue[]) → O(V)
- In the worst case, all V nodes are stored in the queue.
- Graph representation (graph[]) → O(V + E)
- Adjacency list stores edges, requiring space proportional to V + E.
Total Space Complexity:
[ O(V + E) ]
since we store adjacency lists and auxiliary arrays.

'''
    
# With DFS
class Solution:
    def isBipartite(self, graph):
        n = len(graph)
        color = [-1] * n  # -1 means uncolored at the start

        def dfs(node, c):
            color[node] = c  # Color the current node
            for neighbor in graph[node]:
                if color[neighbor] == -1:  # If uncolored
                    if not dfs(neighbor, 1 - c):  # Color with opposite color
                        return False
                elif color[neighbor] == c:  # If same color as current node
                    return False # If this return False, the calling DFS for this neighbor
                    # will also go on returning False till the 1st DFS call
            return True

        for i in range(n):
            if color[i] == -1:  # If uncolored, start DFS
                if not dfs(i, 0):
                    return False

        return True
    
'''
Time Complexity Analysis
- DFS Traversal → O(V + E)
- Each node (V) is visited once.
- Each edge (E) is processed once to check adjacent nodes.
- Outer Loop (Checking All Nodes) → O(V)
- Ensures all components of the graph are considered.
Total Time Complexity:
[ O(V + E) ]
which is standard for DFS-based graph traversal.

Space Complexity Analysis
- Color Array (color[]) → O(V)
- Stores color states for each node.
- Recursive DFS Stack → O(V) (Worst case)
- DFS uses a recursive call stack that can go up to V depth in the worst case (if the graph is a long chain).
- Graph Representation (graph[]) → O(V + E)
- Stores adjacency lists for all edges and nodes.
Total Space Complexity:
[ O(V + E) ]
due to adjacency list storage and recursion overhead.

'''

