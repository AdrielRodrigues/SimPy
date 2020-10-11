# TODO: Verificar o "implements"
import inspect
from util.KShortestPath import KShortestPath as KSP
from sim.Path import Path as Path

class ControlPlane():
    # def __init__(self, xml, events, rsa, pt, vt, traffic):
    def __init__(self, rsa, pt, vt):
        self.rsa = None
        self.pt = pt
        self.vt = vt
        self.mappedFlows = {}
        self.activeFlows = {}
        # mappedPFlows = {}
        # protection = {}
        # Tracer
        # MyStatistics
        # TODO: Interface RSA
        try:
            module = getattr(__import__("algorithm." + rsa), rsa)
            for c in module.__dict__.values():
                if inspect.isclass(c):
                    for i in c.__dict__.values():
                        nm = "algorithm." + rsa
                        if i == nm:
                            self.rsa = c()
                            self.rsa.simulationInterface(pt, vt, self)
                            break
        except ModuleNotFoundError:
            # TODO: Exceção que para a execução da simulação
            pass

    def newEvent(self, event):
        if event.getType() == 'Arrival':
            flow = event.getFlow()
            self.newFlow(flow)
            self.rsa.flowArrival(flow)
            # TODO: Adicionar em Ativos
        elif event.getType() == 'Departure':
            flow = event.getFlow()
            self.rsa.flowDeparture(flow)

    # def getFlow(self, id):
        # return self.activeFlows[id]

    def acceptFlow(self, id, lightpath):
        # TODO: Lidar com algumas exceções. -* Verificar na fonte Java *-
        flow = self.activeFlows.get(id)
        if not self.canAddPathToPT(flow, lightpath):
            return False
        self.addPathToPT(flow, lightpath)
        self.mappedFlows[flow] = lightpath
        flow.setAccepted(True)
        return True

    def removeFlow(self):
        pass

    def blockFlow(self, id):
        if id not in self.activeFlows:
            return False
        flow = self.activeFlows.get(id)
        if flow in self.mappedFlows:
            return False
        self.activeFlows.pop(id)

        # TODO: tracer e statistics

    def canAddPathToPT(self, flow, lightpath):
        for l in lightpath:
            for s in l.getSlotList():
                if self.pt.getLink(s.getLink()).isSlotAvailable(s):
                    return False
        return True

    def addPathToPT(self, flow, lightpath):
        pass

    def newFlow(self, flow):
        self.activeFlows[flow.getID()] = flow