from TrafficInfo import TrafficInfo
from random import choice

class TrafficGenerator():
    def __init__(self, xml, load):
        if xml.find('traffic'):
            traffic = xml.find('traffic')
            self.calls = int(traffic.attrib["calls"])
            self.load = int(traffic.attrib["load"])
            self.maxrate = int(traffic.attrib["max-rate"])
            self.numberCallTypes = 0

            self.callTypes = []

            self.totalWeight = 0
            self.meanRate = 0
            self.meanHoldingTime = 0

            for call in xml.iter('calls'):
                self.totalWeight += float(call.attrib["weight"])

            for call in xml.iter('calls'):
                holdingTime = float(call.attrib["holding-time"])
                rate = int(call.attrib["rate"])
                cos = int(call.attrib["cos"])
                weight = int(call.attrib["weight"])
                self.meanRate += float(rate * (weight/self.totalWeight))
                self.meanHoldingTime += holdingTime * (weight/self.totalWeight)
                self.callTypes.append(TrafficInfo(holdingTime, rate, cos, weight))

            self.numberCallTypes = len(self.callTypes)

    def generateTraffic(self, pt, events, seed):
        weightVector = []
        aux = 0

        for i in range(0, self.numberCallTypes, 1):
            for j in range(self.callTypes[i].getWeight()):
                weightVector.append(i)
                aux += 1

        meanArrivalTime = float((self.meanHoldingTime * (self.meanRate / self.maxrate)) / self.load)

        # type, src, dst
        time = 0.0
        id = 0
        numNodes = pt.getNumNodes()
        # TODO: Distribution

        for c in range(self.calls):
            tipo = choice[weightVector]
