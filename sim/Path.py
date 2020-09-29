class Path():
    def __init__(self, links, channelList, modulation):
        self.links = links
        self.channelList = channelList
        self.modulation = modulation

    def getNumLinks(self):
        return len(self.links)

    def getModulation(self):
        return self.modulation

    def getSlotList(self):
        return self.channelList

    def getLinks(self):
        return self.links

    def getLink(self, link):
        return self.links[link]