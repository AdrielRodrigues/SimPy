# TODO: class Event

class SimulationRunner():
    def __init__(self):
        pass

    def running(self, cp, events):
        # event = Event()
        # Tracer
        # MyStatistics
        for event in events:
            cp.newEvent(event)
            # Tracer add
            # MyStatistics add
            # ControlPlane add