from sim.TrafficInfo import TrafficInfo
from sim.Flow import Flow
from sim.Event import Event
from random import randrange
from random import uniform
import random
from util.Distribution import Distribution
import csv

class TrafficGenerator():
    def __init__(self, xml, load):
        if xml.find('traffic'):
            traffic = xml.find('traffic')
            self.calls = int(traffic.attrib["calls"])
            # self.load = int(traffic.attrib["load"])
            self.load = load
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

        # Extrai os fluxos do arquivo de forma estática

        '''with open("../events/calls.csv", "r") as arq:
            leitor = csv.reader(arq, delimiter=",")
            for linha in leitor:
                id = linha[1]
                src = linha[2]
                dst = linha[3]
                time = linha[8]
                bw = linha[4]
                duration = linha[5]
                cos = linha[6]
                deadline = linha[7]
                events.append(Event(linha[0], Flow(id, src, dst, time, bw, duration, cos, deadline), linha[9]))
                # Flow: id, src, dst, time, bw, duration, cos, deadline
                # type, id, source, destination, rate, duration, cos, deadline, time, time

                # exp = -(ln(random.random(0, 1)) / a'''

        weightVector = []
        aux = 0

        for i in range(0, self.numberCallTypes, 1):
            for j in range(self.callTypes[i].getWeight()):
                weightVector.append(i)
                aux += 1

        meanArrivalTime = float((self.meanHoldingTime * (self.meanRate / self.maxrate)) / self.load)

        time = 0.0
        id = 0
        numNodes = pt.getNumNodes()

        dist1 = Distribution(1, seed)
        dist2 = Distribution(2, seed)
        dist3 = Distribution(3, seed)
        dist4 = Distribution(4, seed)

        for c in range(self.calls):
            type = weightVector[dist1.nextInt(self.totalWeight)]
            src = dst = dist2.nextInt(numNodes)

            while (dst == src):
                # dst = dist2.nextInt(numNodes)
                dst = random.randint(0, numNodes - 1)

            holdingTime = dist4.nextExponential(self.callTypes[type].getHoldingTime())

            newFlow = Flow(id, src, dst, time, self.callTypes[type].getRate(), holdingTime, self.callTypes[type].getCos(), time+(holdingTime * 0.5))

            '''------------------------------------------------------------------
                OS FLUXOS PRECISAM SER ORGANIZADOS EM ORDEM CRESCENTE DE TEMPO
                NO MOMENTO, ELES AINDA ESTÃO SENDO ENFILEIRADOS CONFORME A ORDEM
                EM QUE ELES SÃO INCLUÍDOS
                
                EDIT: A ORDENAÇÃO DOS EVENTOS PARECE SER UM POUCO MAIS COMPLEXA.
                AINDA ASSIM, POR ENQUANTO É MAIS SIMPLES CONSIDERAR QUE OS EVENTOS
                SEGUEM ORDEM CRONOLÓGICA
            ------------------------------------------------------------------'''

            events.addEvent(Event('Arrival', newFlow, time))

            time += dist3.nextExponential(meanArrivalTime)

            events.addEvent(Event('Departure', newFlow, time + holdingTime))

            id += 1

        events.organize()