# Leetcode 323:
'''
In this problem, we have a graph that consists of n nodes. 
We are given an integer n and an array edges where 
each element edges[i] = [a_i, b_i] represents an undirected edge 
between nodes a_i and b_i in the graph. 
The goal is to determine the number of connected components in the graph.
A connected component is a set of nodes in a graph that are connected to each other by paths, 
and those nodes are not connected to any other nodes outside of the component. 
The task is to return the total count of such connected components.

https://algo.monster/liteproblems/323
'''

def count_connected_components(n, edges):
    # Create an adjacency list
    adj_list = [[] for _ in range(n)]
    for edge in edges:
        u, v = edge
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    # Function to perform DFS and mark visited nodes
    def dfs(node, visited):
        stack = [node]
        ''' above is same as:
        stack = []
        stack.append(node)
        '''
        while stack:
            current = stack.pop()
            for neighbor in adj_list[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)
    
    # Initialize visited array
    visited = [False] * n
    connected_components = 0
    
    # Count connected components using DFS
    for i in range(n):
        # If not visited then only perform DFS
        if not visited[i]:
            connected_components += 1 # Increment component count
            visited[i] = True # Mark node as visited
            dfs(i, visited) # Perform DFS to mark all reachable nodes
    
    return connected_components

# Example usage
n = 3
edges = [[0,1], [0,2]]
print(f"The total number of connected components in the graph is {count_connected_components(n, edges)}.")


'''
Logic Explanation
- Graph Representation (Adjacency List)
- We store the graph as an adjacency list (adj_list), where each node maintains a list of its neighbors.
- The input edges defines the connections between nodes.
- We iterate over edges to populate adj_list.
- Depth-First Search (DFS)
- DFS is used to traverse the graph starting from an unvisited node.
- The traversal marks all nodes belonging to the same connected component as visited.
- DFS is implemented using an Iterative Approach with a stack to avoid recursion depth issues.
- Counting Connected Components
- We maintain a visited array to track visited nodes.
- If we find an unvisited node, we perform DFS and increment the counter, as it indicates a new connected component.

Time Complexity Analysis
- Building adjacency list: ( O(E) ), where ( E ) is the number of edges.
- DFS traversal: ( O(V + E) ), since each node and edge is processed once.
- Overall Complexity: ( O(V + E) ), efficient for sparse graphs.
Space Complexity Analysis
- Adjacency list storage: ( O(V + E) ).
- Visited array: ( O(V) ).
- Stack space: ( O(V) ) (in worst case, all nodes in a single component).

'''