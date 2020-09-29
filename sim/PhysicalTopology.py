# Prováveis problemas com tipo do dado. Ex: str ao invés de int
from Link import Link
from util.WeightedGraph import WeightedGraph


class PhysicalTopology():
    def __init__(self, xml):
        if xml.find('physical-topology'):
            pt = xml.find('physical-topology')
            self.name = pt.attrib["name"]
            self.cores = int(pt.attrib["cores"])
            self.slots = int(pt.attrib["slots"])
            self.protection = bool(pt.attrib["protection"])
            self.sharing = bool(pt.attrib["sharing"])
            self.grooming = bool(pt.attrib["grooming"])
            self.slotsBandwidth = float(pt.attrib["slotsBandwidth"])

            self.nodes = []
            self.links = []
            self.matrix = []

            # TODO: Adicionar os elementos como Class em cada lista
            for elem in pt:
                for node in elem.iter('node'):
                    self.nodes.append(node)
                for link in elem.iter('link'):
                    self.links.append(Link(link, self.cores, self.slots))

            for e in range(len(self.nodes)):
                linhaMatrix = []
                for f in range(len(self.nodes)):
                    linhaMatrix.append(None)
                self.matrix.append(linhaMatrix)

            for l in self.links:
                self.matrix[l.getSource()][l.getDestination()] = l


            self.graph = self.doWeightedGraph()
        else:
            # TODO: Lidar com a exceção
            print("ERROR")

    def getGrooming(self):
        return self.grooming

    def getProtection(self):
        return self.protection

    def getNumNodes(self):
        return len(self.nodes)

    def getNumCores(self):
        return self.cores

    def getSlotsCapacity(self):
        return self.slotsBandwidth

    def getNumLinks(self):
        return len(self.links)

    def getNumSlots(self):
        return self.slots

    def getLink(self, link):
        return self.links[link]

    def getLink(self, src, dst):
        return self.matrix[src][dst]

    def doWeightedGraph(self):
        g = WeightedGraph(len(self.nodes))
        for i in range(len(self.nodes)):
            for j in range(len(self.nodes)):
                if self.matrix[i][j] is not None:
                    g.addEdge(i, j, self.matrix[i][j].getWeight())
        return g

    def getGraph(self):
        return self.graph