class TrafficInfo():
    def __init__(self, holdingTime, rate, cos, weight):
        self.holdingTime = holdingTime
        self.rate = rate
        self.cos = cos
        self.weight = weight

    def getHoldingTime(self):
        return self.holdingTime

    def getRate(self):
        return self.rate

    def getCos(self):
        return self.cos

    def getWeight(self):
        return self.weight