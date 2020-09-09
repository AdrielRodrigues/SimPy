# Prováveis problemas com tipo do dado. Ex: str ao invés de int
from Link import Link


class PhysicalTopology():
    def __init__(self, xml):
        if xml.find('physical-topology'):
            pt = xml.find('physical-topology')
            self.name = pt.attrib["name"]
            self.cores = pt.attrib["cores"]
            self.slots = pt.attrib["slots"]
            self.protection = pt.attrib["protection"]
            self.sharing = pt.attrib["sharing"]
            self.grooming = pt.attrib["grooming"]
            self.slotsBandwidth = pt.attrib["slotsBandwidth"]

            self.nodes = []
            self.links = []

            # TODO: Adicionar os elementos como Class em cada lista
            for elem in pt:
                for node in elem.iter('node'):
                    self.nodes.append(node)
                for link in elem.iter('link'):
                    self.links.append(Link(link, self.cores, self.slots))
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
