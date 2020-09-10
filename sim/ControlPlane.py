# TODO: Verificar o "implements"

class ControlPlane():
    def __init__(self, xml, events, rsa, pt, vt, traffic):
        self.rsa = rsa
        self.pt = pt
        self.vt = vt
        mappedFlows = {}
        # mappedPFlows = {}
        # protection = {}
        # Tracer
        # MyStatistics
        # TODO: Interface RSA

    def newEvent(self, event):
        if event == 'arrival':
            pass
        elif event == 'departure':
            pass

    def getFlow(self):
        pass

    def acceptFlow(self):
        pass

    def removeFlow(self):
        pass

    def blockFlow(self):
        pass

    