# TODO: Verificar o Comparator do Java
# TODO: HashMap e Dictionary

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
    def createLightpath(self, links, channelList, modulationLevel):
        # TODO: Lidar com exceção
        # TODO: Ver a função da class LightPath
        src = None
        dst = None

        if canCreateLightpath(links, channelList, modulationLevel):
            createLightpathInPT(links, channelList, modulationLevel)
            src = pt.getLink(links[0]).getSource()
            dst = pt.getLink(links[len(links) - 1]).getDestination()


    def canCreateLightpath(self, links, slots, modulationLevel):
        for l in links:
            for s in slots:
                pass
        return True

    def createLightpathInPT(self, links, slots, modulationLevel):
        pass