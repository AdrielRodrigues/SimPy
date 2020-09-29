class Flow():
    def __init__(self, id, src, dst, time, bw, duration, cos, deadline):
        self.id = id
        self.src = src
        self.dst = dst
        self.time = time
        self.bw = float(bw)
        self.duration = duration
        self.cos = cos
        self.deadline = deadline
        self.accepted = False

    def getRate(self):
        return self.bw