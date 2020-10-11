import math
from sim.Path import Path
from sim.Slot import Slot
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
        path = self.getKShortestPath(self.pt.getGraph(), flow.getSource(), flow.getDestination(), 3)

        if path is None:
            self.cp.blockFlow(flow.getID())
            return

        id = self.vt.createLightpath(path, 0)

        if id >= 0:
            flow.setLinks(path.getLinks())
            flow.setSlotList(path.getSlotList())
            flow.setModulationLevel(0)
            lightpath = []
            lightpath.append(self.vt.getLightPath(id))
            if not self.cp.acceptFlow(flow.getID(), lightpath):
                self.cp.blockFlow(flow.getID())
            return
        if id < 0:
            self.cp.blockFlow(flow.getID())

    def flowDeparture(self, flow):
        pass

    def getKShortestPath(self, graph, src, dst, demand):
        kShortestPaths = KShortestPath()
        kPaths = kShortestPaths.dijkstraKShortestPaths(graph, src, dst, 3)
        if kPaths is None:
            return None
        links = []
        channel = [] # Slots

        for path in kPaths:
            if len(path) > 1:
                links.clear()
                for node in range(0, len(path) - 1):
                    links.append(self.pt.getLink(path[node], path[node + 1]).getID())
                channel = self.getSimilarSlotsInLinks(links, demand)
                if channel is not None:
                    return Path(links, channel, 0) # modulation
            else:
                continue
        a = 3

    # TODO: adicionar funcionalidade para o Sharing

    def getSimilarSlotsInLinks(self, links, demand):
        channel = []
        for i in range(0, self.pt.getNumSlots() - demand):
            firstSlot = i
            lastSlot = i + demand - 1
            core = self.usingSameCore(firstSlot, lastSlot, links)
            if core is not -1:
                for j in range(firstSlot, lastSlot + 1):
                    for l in links:
                        channel.append(Slot(core, j, l))
                return channel
        return None

    def usingSameCore(self, first, last, links):
        for core in range(self.pt.getNumCores()):
            if self.freeSlotInAllLinks(links, first, last, core):
                return core
        return -1

    def freeSlotInAllLinks(self, links, first, last, core):
        for l in links:
            for s in range(first, last + 1):
                if not (self.pt.getLink(l).getSpectrum(core, s)):
                    return False
        return True