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

    def getRate(self):
        return self.bw

    def getSource(self):
        return self.src

    def getDestination(self):
        return self.dst

    def getID(self):
        return self.id

    def setAccepted(self, b):
        self.accepted = b

    def setLinks(self, links):
        self.links = links

    def setSlotList(self, slots):
        self.slotList = slots

    def setModulationLevel(self, modulation):
        self.modulationLevel = modulation