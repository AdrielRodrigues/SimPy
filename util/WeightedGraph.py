class WeightedGraph():
    def __init__(self, n):
        self.numNodes = n
        self.edges = []
        for c in range(n):
            edgeslinha = []
            for d in range(n):
                edgeslinha.append(None)
            self.edges.append(edgeslinha)

    def addEdge(self, source, destination, weight):
        self.edges[source][destination] = weight