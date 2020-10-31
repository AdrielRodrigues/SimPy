import random


class Connection:
    # dtr maximum data transference rate
    # oc oscillation
    # @param lt network latency (ms)
    def __init__(self, dtr, oc_range, lt, overhead=0.10):
        self.overhead = overhead
        self.dtr = dtr*(1-overhead)
        self.oc_range = oc_range
        self.average_dtr = self.average()
        self.lt = lt/1000

    # this methode will define how the connection vary due to "random"
    # factors that can affect the network
    def rand_transfer_rate(self):
        return self.dtr - (2*random.random()*self.oc_range)

    # this methode defines the average data transfer rate of an connection
    def average(self):
        return self.dtr - self.oc_range


class PreCopyMigrationOPS:
    # img_size is the total size of the memory to be transferred (MB)
    # wr, write rate of the vm (MB/s)
    # dt is the downtime that the vm want to achieve (ms)
    # tsc is the time to stop-and-copy faze
    # tt is the time threshold for a migration to be declared as failed (s)
    # fm = force migration
    def __init__(self, img_size, wr, dt, connection, tt=60, fm=False):
        self.img_size = img_size
        self.wr = wr
        self.dt = dt / 1000
        self.connection = connection
        self.memory_left = img_size
        self.tsc = -1
        self.tt = tt
        self.fm = fm

    # bw bandwidth (Mb/s)
    # lt latency time (seconds)
    def send(self, bw):
        time = self.memory_left / bw
        # not the accurate way of doing it. it will overestimate the
        # amount of data that really needs to be transferred most of
        # the times.
        # placeholder
        dirtied_mem = time*self.wr*((self.img_size-self.memory_left+self.memory_left/2)/self.img_size)
        self.memory_left = dirtied_mem if dirtied_mem < self.img_size else self.img_size
        return time, self.memory_left <= self.tsc

    # start de migration process, return the total migration time and te downtime. If the
    # migration is cancelled due to the time limit, it returns the downtime as -1
    def migrate(self):
        self.tsc = self.connection.average_dtr * self.dt
        total_time, final_round = self.send(self.connection.rand_transfer_rate())
        # used fo debugging
        # print(total_time, final_round, self.memory_left)
        while not final_round:
            time, final_round = self.send(self.connection.rand_transfer_rate())
            total_time += time
            # print(total_time, final_round, self.memory_left)
            if total_time >= self.tt:
                if not self.fm:
                    print('minimal downtime could not be achieved (migration cancelled)')
                    return total_time, -1
                else:
                    print('minimal downtime could not be achieved (migration completed anyway)')
                    break
        downtime = self.memory_left / self.connection.rand_transfer_rate() + self.connection.lt
        total_time += downtime
        return total_time, downtime
