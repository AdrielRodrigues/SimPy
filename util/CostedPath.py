class CostedPath():
    def __init__(self, graph, costedpath = None):
        self.graph = graph
        self.array = []
        if costedpath is not None:
            for each in costedpath.getArray():
                self.array.append(each)
        self.cost = 0

    def add(self, n):
        if len(self.array) == 0:
            self.array.append(n)
        else:
            u = self.getLast()
            self.cost += self.graph.getWeight(u, n)
            self.array.append(n)

    def getCost(self):
        return self.cost

    def getArray(self):
        return self.array

    def getLast(self):
        return self.array[len(self.array) - 1]

    def containArray(self, n):
        if n in self.array:
            return True
        else:
            return False