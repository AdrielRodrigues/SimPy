import xml.etree.ElementTree as ET
from sim.PhysicalTopology import PhysicalTopology
from sim.VirtualTopology import VirtualTopology
from sim.EventScheduler import EventScheduler
from sim.TrafficGenerator import TrafficGenerator
# from MyStatistics import MyStatistics
from sim.ControlPlane import ControlPlane
from sim.SimulationRunner import SimulationRunner


class Simulator():
    def __init__(self):
        self.trace = False
        self.verbose = False
        self.failure = False

    # TODO: Lidar com exceções
    def execute(self, simConfigFile, trace, verbose, failure, forcedLoad, numberOfSimulations):
        self.trace = trace
        self.verbose = verbose
        self.failure = failure

        # TODO: Verificar a solução JSON para as configs da topologia
        mytree = ET.parse(simConfigFile)
        myroot = mytree.getroot()

        ##### OutputManager #####

        # TODO: Eventualmente consertar os laços For
        # TODO: Implementar o TimeMillis
        for seed in range(1, numberOfSimulations + 1, 1):

            # begin = time

            ##### PhysicalTopology #####
            pt = PhysicalTopology(myroot)

            ##### Virtual Topology #####
            vt = VirtualTopology(myroot, pt)

            ##### Event Scheduler #####
            # events = EventScheduler()
            events = []

            ##### Traffic Generator #####
            traffic = TrafficGenerator(myroot, forcedLoad)
            traffic.generateTraffic(pt, events, seed)

            ##### MyStatistics #####
            # st = MyStatistics()

            ##### Pega RSA #####
            if myroot.findall('rsa'):
                algorithm = myroot.find('rsa').attrib["module"]

            ##### ControlPlane #####
            cp = ControlPlane(algorithm, pt, vt)

            ##### SimulationRunner #####
            action = SimulationRunner()
            action.running(cp, events)
        return 1
