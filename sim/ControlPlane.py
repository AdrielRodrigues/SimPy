# TODO: Verificar o "implements"
import inspect

class ControlPlane():
    # def __init__(self, xml, events, rsa, pt, vt, traffic):
    def __init__(self, rsa, pt, vt):
        self.rsa = None
        self.pt = pt
        self.vt = vt
        mappedFlows = {}
        activeFlows = {}
        # mappedPFlows = {}
        # protection = {}
        # Tracer
        # MyStatistics
        # TODO: Interface RSA
        try:
            module = getattr(__import__("algorithm." + rsa), rsa)
            for c in module.__dict__.values():
                if inspect.isclass(c):
                    self.rsa = c()
                    self.rsa.simulationInterface(pt, vt, self)
        except ModuleNotFoundError:
            # TODO: Exceção que para a execução da simulação
            pass

    def newEvent(self, event):
        if event.getType() == 'Arrival':
            flow = event.getFlow()
            self.rsa.flowArrival(flow)
            # TODO: Adicionar em Ativos
        elif event.getType() == 'Departure':
            flow = event.getFlow()
            self.rsa.flowDeparture(flow)

    # def getFlow(self, id):
        # return self.activeFlows[id]

    def acceptFlow(self):
        pass

    def removeFlow(self):
        pass

    def blockFlow(self):
        pass

    