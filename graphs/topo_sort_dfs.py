# Topological Sort
# This sort is applicable on DAG only
# By DFS

# https://takeuforward.org/data-structure/topological-sort-algorithm-dfs-g-21/

from collections import defaultdict, deque
class Solution:
    def topoSort(self, V, adj):
        visited = [False] * V
        stack = []

        def dfs(node):
            visited[node] = True
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
            # Push the node into stack after exploring all its dependencies
            # This ensures that the node is processed after all its neighbors
            # have been processed, which is essential for topo sort
            stack.append(node)

        # connected components
        for i in range(V):
            if not visited[i]:
                dfs(i)

        return stack[::-1]  # Return the stack in reverse order for topological sort




# Driver code
if __name__ == "__main__":
    V = 6
    adj = defaultdict(list)

    adj[2].append(3)
    adj[3].append(1)
    adj[4].append(0)
    adj[4].append(1)
    adj[5].append(0)
    adj[5].append(2)

    solution = Solution()
    ans = solution.topoSort(V, adj)
    
    print("Topological Order:", ans)


'''
Time Complexity
- DFS Traversal: Each node is visited exactly once during DFS (O(V)).
- Processing Edges: For every node, we iterate through its adjacency list, visiting each edge once (O(E)).
- Stack Reversal: Reversing the stack takes O(V).
Total Time Complexity: [ O(V + E) ] This is the optimal time complexity for topological sorting using DFS.

Space Complexity
- Visited Array (visited[]): Stores V elements → O(V).
- Stack (stack[]): In the worst case, all V nodes are stored → O(V).
- Adjacency List (adj[]): Stores E edges → O(V + E).
Total Space Complexity: [ O(V + E) ] This includes adjacency list storage and DFS recursion overhead.

'''