from data_structures.Graph import Graph

def depth_first_traversal(graph, v, discovered):
    """
    Traverse a graph with a preorder traversal.
    Prevent infinite loops by keeping track of the
    vertices that are already discovered and not
    visit them again.
    """
    discovered[v] = True    # mark current node as discovered
    print(v, end=" ")       # print current node

    # do for every edge (v -> u)
    for u in graph.adjList[v]:
        if not discovered[u]:
            depth_first_traversal(graph, u, discovered)

# Driver
if __name__ == '__main__':

    # List of graph edges as per above diagram
    edges = [
        # Notice that node 0 is unconnected node
        (1, 2), (1, 7), (1, 8), (2, 3), (2, 6), (3, 4),
        (3, 5), (8, 9), (8, 9), (8, 12), (9, 10), (9, 10)
    ]

    # Set number of vertices in the graph (0-12)
    N = 13

    # create a graph from edges
    graph = Graph(edges, N)

    # stores vertex is discovered or not
    discovered = [False] * N

    # Do DFS traversal from all undiscovered node to
    # cover all unconnected components of graph.
    for i in range(N):
        if not discovered[i]:
            depth_first_traversal(graph, i, discovered)