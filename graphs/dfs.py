#DFS using list data structure

#TC = O(V) + O(2E) = O(V + E)  where 2E is the summation of degrees
# 2E for undirected and E for directeds
#SC = O(V) + O(V) = O(V) visited list of size V 
#and in worst case the stack space used by recursion will be V
#eg. in case of skewed graph 1->2->3->4

# Function to create an adjacency list from user input
def create_graph(num_nodes, num_edges):
    #graph = []
    graph = {}

    # Initialize graph (adj list) with empty lists for each node
    for i in range(num_nodes):
        node = input(f"Enter the name of node {i+1}: ")
        graph[node] = []

    # Take input for each edge and update adjacency list
    for i in range(num_edges):
        u, v = input(f"Enter edge {i+1} (format: node1 node2): ").split()
        graph[u].append(v)  # Directed graph (u -> v)
        graph[v].append(u)  # For undirected graph, add both (u -> v) and (v -> u)

    return graph

#Recursive DFS implementation
#def dfs_recursive(graph, node, visited):
# graph -> adj list
def dfs_recursive(graph, node, visited = None):    
    # Mark node as visited by adding to the visited list
    # Initialize the visited list if it's the first call
    if visited is None:
        visited = []
    #For 1st time its the start node
    visited.append(node)  
    print(node, end = ' ') # Print or do some processing with the node

    #Recur for all adjacent vertices
    for neighbor in graph[node]:     #O(2E) 
        if neighbor not in visited:  # Check if neighbor is not in the visited list
            dfs_recursive(graph, neighbor, visited)

def dfs_iterative(graph, s):
    stack = [s] # Stack to hold nodes to visit
    visited = []  # List to track visited nodes

    while stack:          #while stack is not empty it'll run
        node = stack.pop()      # Get the last node (DFS goes deep)

        if node not in visited:
            print(node, end = ' ')   #process the node
            visited.append(node)       #mark node as visited

            #add all unvisited neighbors to the stack
            for neighbor in reversed(graph[node]):   # Reversed to maintain DFS order
                if neighbor not in visited:
                    stack.append(neighbor)


# Main function to execute the DFS algorithms
def main():
    # Take input from the user for the number of nodes and edges
    num_nodes = int(input("Enter the number of nodes: "))
    num_edges = int(input("Enter the number of edges: "))

    # Create the graph using an adjacency list
    graph = create_graph(num_nodes, num_edges)
    
    print("\nAdjacency List Representation of Graph:")
    for node, neighbors in graph.items():
        print(f"{node}: {', '.join(neighbors)}")

    # Take input for starting node
    start_node = input("\nEnter the starting node for DFS: ")

    # Run Recursive DFS
    print("\nDFS (Recursive):")
    #visited = [] # List to keep track of visited nodes
    #dfs_recursive(graph, start_node, visited)
    dfs_recursive(graph, start_node)

    # Run Iterative DFS
    print("\n\nDFS (Iterative):")
    dfs_iterative(graph, start_node)

if __name__ == "__main__":
    main()



# Simple implementation
from collections import deque

# Recursive implementation
def dfs_recursive(adj, node, visited):
    # Step 1: Mark the current node as visited
    visited[node] = True

    # Step 2: Process the current node (e.g., print it)
    print(node, end=" ")

    # Step 3: Recursively visit all unvisited neighbors
    for neighbor in adj[node]:
        if not visited[neighbor]:
            dfs_recursive(adj, neighbor, visited)


# Iteratiive implementation
def dfs_iterative(adj, start):
    # Create a stack to manage nodes during DFS traversal
    stack = deque()

    # Initialize visited list to track which nodes have been explored
    visited = [False] * len(adj)

    # Start DFS by pushing the initial node onto the stack
    stack.append(start)

    # Continue traversal until the stack is empty
    while stack:
        # Pop the top node from the stack (LIFO behavior)
        node = stack.pop()

        # If the node hasn't been visited yet, process it
        if not visited[node]:
            visited[node] = True  # Mark the node as visited
            print(node, end=" ")  # Print or process the node

            # Traverse all adjacent nodes
            # Reverse the adjacency list to maintain left-to-right order
            for neighbor in reversed(adj[node]):
                if not visited[neighbor]:
                    stack.append(neighbor)  # Push unvisited neighbors onto the stack

if __name__ == "__main__":
    v = 5
    adj = [[] for _ in range(v)]

    add_edge(adj, 0, 1)
    add_edge(adj, 0, 2)
    add_edge(adj, 1, 3)
    add_edge(adj, 1, 4)
    add_edge(adj, 2, 4)

    print("\nDFS Recursive starting from 0:")
    visited = [False] * v
    dfs_recursive(adj, 0, visited)

    print("\nDFS Iterative starting from 0:")
    dfs_iterative(adj, 0)