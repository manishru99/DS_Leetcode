# G-32. Dijkstra's Algorithm - Using Set

from sortedcontainers import SortedSet

class Solution:
    def dijkstra(self, V, adj, S):
        # Initialize a sorted set to act like a priority queue:
        # it stores pairs of (distance, node), always sorted by distance.
        st = SortedSet()
        # Initialize distances: set all distances to infinity,
        # except the source node which is 0.
        dist = [float('inf')] * V
        dist[S] = 0
        st.add((0, S))  # Add the source to the set with distance 0

        # Process the set until all reachable nodes are visited
        while st:
            dis, node = st.pop() # Extract the node with the smallest distance

            # Traverse all neighbors of the current node
            for neighbor in adj[node]:
                adjNode, weight = neighbor # Extract neighbor and edge weight

                # If a shorter path to adjNode is found through current node
                if dis + weight < dist[adjNode]:
                    # This is the difference of using set vs PQ for Dijkstra's
                    # If the node was already in the set with a longer distance, remove it
                    if dist[adjNode] != float('inf'):
                        st.discard(dist[adjNode], adjNode)
                    # Update to the shorter distance and insert the new pair
                    dist[adjNode] = dis + weight
                    st.add((dist[adjNode], adjNode))
        # Return the computed shortest distances from the source node
        return dist

'''
Time Complexity: O((V + E) log V) in practice, O(E log V) in most cases
- You perform up to V insertions/deletions in the set, each costing O(log V).
- Each edge (up to E) may cause an update and reordering → O(log V) per update.
- So overall complexity is:
- Worst-case: O((V + E) log V)
- Why not O(V log V + E)? Because you're using a SortedSet which allows deletions of arbitrary elements (discard), not just from the front like a heap.
In graphs with dense edges, this set-based version performs similarly to heap-based Dijkstra.


🧠 Space Complexity: O(V + E)
- O(V) for:
- The dist array storing shortest distances
- The set storing up to V pairs (distance, node)
- O(E) for the adjacency list

'''

