# Bellman Ford 

def bellman_ford(edges, V, source):
    # edges: list of (u, v, weight) representing directed edges from u to v with weight w
    # V: total number of vertices
    # source: starting vertex for shortest path calculation

    # Step 0: Initialize distances from source to all vertices as infinity
    dist = [float('inf')] * V
    dist[source] = 0  # Distance to source is 0

    # Step 1: Relax all edges V-1 times
    # In a graph with V vertices, the longest possible shortest path has at most V-1 edges
    for _ in range(V - 1):
        for u, v, w in edges:
            # If the path from source to v via u is shorter, update it
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Step 2: Check for negative-weight cycles
    # If we can still relax any edge, then a negative cycle exists
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            raise ValueError("Graph contains a negative-weight cycle")

    # Return the shortest distances from source to all vertices
    return dist