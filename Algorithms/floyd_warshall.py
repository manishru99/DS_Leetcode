# Floyd Warshall (All Pair Shortest Path)

# TC = O(V3)
# Three nested loops over all vertices: 
# intermediate k, source i, destination j
# SC = O(V2)
# Stores a 2D distance matrix of size V × V

def floyd_warshall(graph):
    # graph: 2D matrix where graph[i][j] is the weight of the edge from node i to node j
    V = len(graph)  # Number of vertices

    # Step 0: Initialize distance matrix as a deep copy of the input graph
    # This ensures we don't modify the original graph
    dist = [row[:] for row in graph]

    # Step 1: DP loop
    # Try every node k as an intermediate between i and j
    for k in range(V):  # Intermediate node
        for i in range(V):  # Source node
            for j in range(V):  # Destination node
                # If the path from i to j through k is shorter than the current known path, update it
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    # Step 2: Detect negative-weight cycles
    # If the distance from any node to itself becomes negative, a cycle exists
    for i in range(V):
        if dist[i][i] < 0:
            raise ValueError("Graph contains a negative-weight cycle")

    # Return the final distance matrix containing shortest paths between all pairs
    return dist