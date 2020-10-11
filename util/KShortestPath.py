from util.CostedPath import CostedPath

class KShortestPath():
    def __init__(self):
        pass

    def dijkstraKShortestPaths(self, graph, src, dst, k):
        P = [] # ArrayList de CostedPath
        count = [] # array
        for i in range(graph.size()):
            count.append(0)
        B = [] # ArrayList CostedPath
        Ps = CostedPath(graph)
        Ps.add(src)
        B.append(Ps)
        while not len(B) == 0 and count[dst] < k:
            Pu = self.minCost(B)
            u = Pu.getLast()
            B.remove(Pu)
            count[u] += 1
            if u == dst:
                P.append(Pu)
            else:
                if count[u] <= k:
                    n = graph.neighbors(u)
                    for v in n:
                        if not Pu.containArray(v):
                            Pv = CostedPath(graph, Pu)
                            Pv.add(v)
                            B.append(Pv)
        if len(P) < k:
            return None
        kPaths = []
        for i in range(0, k):
            kpath = []
            for each in P[i].getArray():
                kpath.append(each)
            kPaths.append(kpath)

        return kPaths

    def minCost(self, paths):
        if len(paths) == 0:
            return None
        minCost = paths[0]
        for p in paths:
            if p.getCost() < minCost.getCost():
                minCost = p
        return minCost