class Link():
    def __init__(self, xml, cores, slots):
        # TODO: Adicionar o tipo de cada uma variável
        self.id = int(xml.attrib["id"])
        self.src = int(xml.attrib["source"])
        self.dst = int(xml.attrib["destination"])
        self.delay = float(xml.attrib["delay"])
        self.bandwidth = float(xml.attrib["bandwidth"])
        self.weight = float(xml.attrib["weight"])
        # TODO: slots and cores
        self.freeSlots = []
        self.modulationLevel = []

        # TODO: Modificar o tipo de cores e slots
        for c in range(cores):
            unit = []
            mod = []
            for s in range(slots):
                unit.append(True)
                mod.append(-1)
            self.freeSlots.append(unit)
            self.modulationLevel.append(mod)

    def getSpectrum(self):
        return self.freeSlots

    def getSpectrum(self, core):
        return self.freeSlots[core]

    def getSpectrum(self, core, slot):
        return self.freeSlots[core][slot]

    def getID(self):
        return self.id

    def getSource(self):
        return self.src

    def getDestination(self):
        return self.dst

    def getWeight(self):
        return self.weight

    def getDelay(self):
        return self.delay

    def isSlotAvailable(self, slot):
        if not self.freeSlots[slot.getCore()][slot.getSlot()]:
            return False
        return True

    def reserveSlot(self, slot):
        self.freeSlots[slot.getCore()][slot.getSlot()] = False

    def releaseSlot(self, slot):
        self.freeSlots[slot.getCore()][slot.getSlot()] = True

    def setModulationLevel(self, slot, modulation):
        self.modulationLevel[slot.getCore()][slot.getSlot()] = modulation