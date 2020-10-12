class Flow():
    def __init__(self, id, src, dst, time, bw, duration, cos, deadline):
        self.id = float(id)
        self.src = int(src)
        self.dst = int(dst)
        self.time = float(time)
        self.bw = float(bw)
        self.duration = float(duration)
        self.cos = int(cos)
        self.deadline = float(deadline)
        self.accepted = False
        self.links = None
        self.slotList = None
        self.modulationLevel = None

    def getID(self):
        return self.id

    def getSource(self):
        return self.src

    def getDestination(self):
        return self.dst

    def getTime(self):
        return self.time

    def getRate(self):
        return self.bw

    def getDuration(self):
        return self.duration

    def getCOS(self):
        return self.cos

    def getDeadline(self):
        return self.deadline

    def getAccepted(self):
        return self.accepted

    def getLinks(self):
        return self.links

    def getSlotList(self):
        return self.slotList

    def getModulationLevel(self):
        return self.modulationLevel

    def setAccepted(self, b):
        self.accepted = b

    def setLinks(self, links):
        self.links = links

    def setSlotList(self, slotList):
        self.slotList = slotList

    def setModulation(self, modulationLevel):
        self.modulationLevel = modulationLevel