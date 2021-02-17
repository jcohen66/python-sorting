class Graph(object):
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict

    def get_vertices(self):
        '''
        Get the keys of the dictionary.
        '''
        return list(self.gdict.keys())

    def edges(self):
        return self.find_edges()

    def find_edges(self):
        edge_name = []
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict:
                if (nxtvrtx, vrtx) not in edge_name:
                    edge_name.append({vrtx, nxtvrtx})
        return edge_name

    def add_vertex(self, vrtx):
        if vrtx not in self.gdict:
            self.gdict[vrtx] = []

    def add_edge(self, edge):
        edge = set(edge)
        (vrtx1, vrtx2) = tuple(edge)
        if vrtx1 in self.gdict:
            self.gdict[vrtx1].append(vrtx2)
        else:
            self.gdict[vrtx1] = [vrtx2]

# Driver
graph_elements = { "a" : ["b", "c"],
                   "b" : ["a", "d"],
                   "c" : ["a", "d"],
                   "d" : ["e"],
                   "e" : ["d"]
                   }

g = Graph(graph_elements)

#print(g.get_vertices())
print(g.edges())
g.add_vertex("f")
print(g.get_vertices())

g.add_edge({"a","e"})
g.add_edge({"a", "c"})

print(g.edges())