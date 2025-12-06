# Dijkstra’s algorithm 

import heapq
from collections import defaultdict

def dijkstra(graph, start):
    # graph: dict of node -> list of (neighbor, weight) ie adj list
    # Initialize all distances to infinity
    dist = defaultdict(lambda: float('inf'))
    dist[start] = 0  # Distance to start node is 0

    visited = set()  # Track visited nodes to avoid reprocessing
    # heap -> <dist, node>
    heap = [(0, start)]  # Min-heap to always process the node with the smallest distance

    while heap:
        # Pop the node with the smallest known distance
        current_dist, node = heapq.heappop(heap)

        # Skip if already visited
        if node in visited:
            continue # skip currr iteration
        # if not vis
        visited.add(node)

        # Explore all neighbors of the current node
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                # Calculate new tentative distance
                new_dist = current_dist + weight

                # If it's shorter than the known distance, update it
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    # Push the updated distance and neighbor into the heap
                    heapq.heappush(heap, (new_dist, neighbor))

    # Return the final shortest distances from the start node to all reachable nodes
    return dict(dist)