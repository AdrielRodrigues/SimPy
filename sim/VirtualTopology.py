# TODO: Verificar o Comparator do Java
# TODO: HashMap e Dictionary
from sim.Lightpath import Lightpath


class VirtualTopology():
    def __init__(self, xml, pt):
        if xml.find('virtual-topology'):
            vt = xml.find('virtual-topology')
            self.name = vt.attrib["name"]
        self.nodes = pt.getNumNodes()
        self.lightpaths = {}
        self.pt = pt
        self.nextLightpathID = 0

    # TODO: Escolher entre ou dar suporte para Path ou Links+Slots
    def createLightpath(self, path, modulationLevel):
        # TODO: Lidar com exceção

        if len(path.getLinks()) < 1:
            pass
        else:
            if self.canCreateLightpath(path.getSlotList(), modulationLevel):
                self.createLightpathInPT(path.getSlotList(), modulationLevel)
                src = self.pt.getLink(path.getLink(0)).getSource()
                dst = self.pt.getLink(path.getLink(path.getNumLinks()-1)).getDestination()
                if src == dst:
                    dst = self.pt.getLink(path.getLink(path.getNumLinks() - 2)).getDestination()
                lp = Lightpath(self.nextLightpathID, src, dst, path, modulationLevel)
                self.lightpaths[id] = lp
                self.nextLightpathID += 1
                return id
            return -1


    def canCreateLightpath(self, slots, modulationLevel):
        for s in slots:
            if self.pt.getLink(s.getLink()).isSlotAvailable(s):
                return False
        return True

    def createLightpathInPT(self, slots, modulationLevel):
        for s in slots:
            self.pt.getLink(s.getLink()).reserveSlot(s)
            self.pt.getLink(s.getLink()).setModulationLevel(s, modulationLevel)

    def removeLightPath(self, id):
        if id < 0:
            pass
        else:
            if id not in self.lightpaths:
                return False
            lp = self.lightpaths.get(id)
            self.removeLightpathFromPT(lp.getPath().getSlotList())
            src = lp.getSource()
            dst = lp.getDestination()
            self.lightpaths.pop(id)

    def removeLightpathFromPT(self, slots):
        for s in slots:
            self.pt.getLink(s.getLink()).releaseSlot(s)