import xml.etree.ElementTree as ET
from PhysicalTopology import PhysicalTopology
from VirtualTopology import VirtualTopology
# from EventScheduler import EventScheduler
from TrafficGenerator import TrafficGenerator
# from MyStatistics import MyStatistics
# from ControlPlane import ControlPlane
# from SimulationRunner import SimulationRunner

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

            ##### Traffic Generator #####
            traffic = TrafficGenerator(myroot, forcedLoad)
            traffic.generateTraffic(pt, 1, seed)

            ##### MyStatistics #####
            # st = MyStatistics()

            ##### Pega RSA #####
            if myroot.findall('rsa'):
                algorithm = myroot.find('rsa').attrib["module"]
                print(algorithm)

            ##### ControlPlane #####
            # cp = ControlPlane()

            ##### SimulationRunner #####
            # action = SimulationRunner()
        return 1