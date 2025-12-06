from collections import deque

#For BFS: Queue used
#TC = O(V) + O(2E) = O(V+E)  -no of vertices + no of edges
#For every node we traverse all the neighboring nodes
#i.e. for every node in queue inside for loop will run for the node's degree 
#SC = O(V) - queue + visited list + BFS list

# BFS from given source s
def bfs(adj, s):
    # Create a queue for BFS
    q = deque()

    # Initially mark all the vertices as not visited
    # When we push a vertex into the q, we mark it as 
    # visited
    visited = [False] * len(adj) 
    # Use len(adj) when 0-based indexing, len(adj)+1 for 1-based 

    # Mark the source node as visited and enqueue it
    visited[s] = True
    q.append(s)

    #iterate over the queue
    while q:
        #dequeue a vertex from the queue and print it
        curr = q.popleft()
        print(curr, end = " ")

        # Get all adjacent vertices of the dequeued 
        # vertex. If an adjacent has not been visited, 
        # mark it visited and enqueue it
        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                q.append(x)



# Function to add an edge to the graph
def add_edge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)


# Example usage
if __name__ == "__main__":
  
    # Number of vertices in the graph
    v = 5

    # Adjacency list representation of the graph
    adj = [[] for _ in range(v)]

    # Add edges to the graph
    add_edge(adj, 0, 1)
    add_edge(adj, 0, 2)
    add_edge(adj, 1, 3)
    add_edge(adj, 1, 4)
    add_edge(adj, 2, 4)

    # Perform BFS traversal starting from vertex 0
    print("BFS starting from 0: ")
    bfs(adj, 0)


