class Slot():
    def __init__(self, core, slot, link):
        self.core = core
        self.slot = slot
        self.link = link

    def getCore(self):
        return self.core

    def getSlot(self):
        return self.slot

    def getLink(self):
        return self.link