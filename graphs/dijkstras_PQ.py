# G-32. Dijkstra's Algorithm - Using Priority Queue

import heapq

class Solution:
    # V - number of vertices (or nodes) 
    # S - source node — the starting point from which we want to calculate 
    # the shortest distances to all other nodes.
    def dijkstra(self, V, adj, S):
        # Step 1: Initialize all distances as infinity
        # This list stores the shortest known distance from source S to every vertex
        # Initialize distances to all vertices as infinity
        dist = [float('inf')] * V
        dist[S] = 0  # Distance to source is 0

        # Step 2: Priority queue (min-heap) to fetch the next closest unvisited node
        # Min-heap priority queue as (distance, vertex)
        pq = [(0, S)]

        # Step 3: Process the queue until all reachable nodes are visited
        while pq:
            # Get node with the smallest known distance
            dis, node = heapq.heappop(pq)

            # Step 4: Traverse all adjacent vertices (neighbors) of current node
            for neighbor in adj[node]:
                v, w = neighbor  #  v is the adjacent node, w is the edge weight
                # Step 5: Check if a shorter path to v is found through this node
                if dis + w < dist[v]:
                    # Update the shortest path to v
                    dist[v] = dis + w
                    heapq.heappush(pq, (dist[v], v))
        # Step 6: Return the list of shortest distances from source to all vertices
        return dist

'''
Time Complexity: O((V + E) log V)
- Priority queue operations (heapq.heappush and heappop) take O(log V) time.
- For each of the V vertices, we may insert/update their distances in the heap.
- Each edge is examined at most once when exploring adjacent nodes, contributing E operations.
- So the total cost is O((V + E) log V)
This is assuming a binary heap and an adjacency list representation.


🧠 Space Complexity: O(V + E)
- The dist array stores one entry per vertex → O(V)
- The adjacency list stores up to E edges → O(E)
- The priority queue can hold up to V elements at a time → O(V)
So the overall space used is O(V + E).

'''
if __name__ == "__main__":
    V, E, S = 3, 3, 2
    adj = [[] for _ in range(V)]

    # Manually inserting edges (u -> v with weight w)
    adj[0].append([1, 1])
    adj[0].append([2, 6])
    adj[1].append([2, 3])
    adj[1].append([0, 1])
    adj[2].append([1, 3])
    adj[2].append([0, 6])

    obj = Solution()
    res = obj.dijkstra(V, adj, S)

    print(" ".join(map(str, res)))
