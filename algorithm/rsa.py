import math
# from Path import Path
from util.KShortestPath import KShortestPath
class rsa():
    def __init__(self):
        pass

    def simulationInterface(self, pt, vt, cp):
        self.pt = pt
        self.vt = vt
        self.cp = cp

    def flowArrival(self, flow):
        id = -1
        guardBand = 1
        demandInSlots = math.ceil(flow.getRate() / self.pt.getSlotsCapacity())
        # TODO: kShortestPath()
        # TODO: if path is null
        # TODO: id = vt.createLightPath
        # TODO: set info sobre o path
        # TODO: cp.acceptFlow
        # TODO: else

    def flowDeparture(self, flow):
        pass

    def getKShortestPath(self, graph, src, dst, demand):
        k = 3
        kShortestPaths = KShortestPath()
        kShortestPaths.dijkstraKShortestPaths(graph, src, dst, k)
