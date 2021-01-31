from data_structures.Graph import Graph
from collections import deque

def iterativeDFS(graph, v, discovered):
    """
    Perform iterative DFS on graph g starting
    from vertex v
    """

    # Create a stack used to do iterative DFS
    stack = deque()

    # push the source node into stack
    stack.append(v)

    # loop til stack is empty
    while stack:

        # Pop a vertex from stack
        v = stack.pop()

        # if the vertex is already discovered yet, ignore it
        if discovered[v]:
            continue

        """
        We will reach here if the popped vertex v
        is not discovered yet.  We print it and process
        its undiscovered adjacent nodes into stack.
        """
        discovered[v] = True
        print(v, end=" ")

        # do for every edge (v -> u)
        adj = graph.adjList[v]
        for i in reversed(range(len(adj))):
            u = adj[i]
            if not discovered[u]:
                stack.append(u)

# Driver

# List of graph edges as per above diagram
edges = [
    # Notice that node 0 is unconnected node
    (1, 2), (1, 7), (1, 8), (2, 3), (2, 6), (3, 4),
    (3, 5), (8, 9), (8, 12), (9, 10), (9, 11)
    # , (6, 9) # introduce cycle
]

# Set number of vertices in the graph (0-12)
N = 13

# create a graph from edges
graph = Graph(edges, N )

# stores vertex is discovered or not
discovered = [False] * N

# Do iterative DFS traversal from all
# undiscovered nodes to cover all
# unconnected components of graph.
for i in range( N ):
    if not discovered[i]:
        iterativeDFS(graph, i, discovered)