import random


class MigrationConnection:
    """
    dtr - maximum data transference rate
    oc - oscillation
    lt - network latency (ms)
    """
    def __init__(self, dtr, oc_range, lt, overhead=0.10):
        self.overhead = overhead
        self.dtr = dtr*(1-overhead)
        self.oc_range = oc_range
        self.average_dtr = self.average()
        self.lt = lt/1000

    # this methode will define how the connection vary due to "random"
    # factors that can affect the network
    def rand_transfer_rate(self):
        return self.dtr + (2*random.triangular(-1, 1, 0)*self.oc_range)

    # this methode defines the average data transfer rate of an connection
    def average(self):
        return self.dtr - self.oc_range


class PreCopyMigrationOPS:
    """
    img_size   - is the total size of the memory to be transferred ( MB )
    wr         - write rate of the vm ( MB/s )
    dt         - is the downtime that the vm want to achieve ( ms )
    tsc        - the size threshold to start the stop and copy faze ( MB )
    time_limit - is the time threshold for a migration to be declared as failed ( s )
    fm         - if True, it completes the migration independent of the final downtime
                when (and if) the time reaches the limit. Else, the migration will be
                cancelled.
    """
    def __init__(self, img_size, wr, dt, connection, time_limit=10000, fm=False):
        self.img_size = img_size
        self.wr = wr
        self.dt = dt / 1000
        self.connection = connection
        self.memory_left = img_size
        self.tsc = self.connection.average_dtr * self.dt
        self.time_limit = time_limit
        self.fm = fm


    '''
    def send(self, bw: float):
        time = self.memory_left / bw
        dirtied_mem = time*self.wr*((self.img_size-self.memory_left+self.memory_left/2)/self.img_size)
        self.memory_left = dirtied_mem if dirtied_mem < self.img_size else self.img_size
        return time, self.memory_left <= self.tsc
    '''

    def send_pages(self):
        time = (self.memory_left / self.connection.rand_transfer_rate())
        dirtied_mem = time * self.wr * ((self.img_size - self.memory_left/2) / self.img_size)
        self.memory_left = dirtied_mem if dirtied_mem < self.img_size else self.img_size
        return time, self.memory_left <= self.tsc
        pass

    # start de migration process, return the total migration time and te downtime. If the
    # migration is cancelled due to the time limit, it returns the downtime as -1
    def migrate(self):

        total_time, final_round = self.send_pages()
        while not final_round:
            time, final_round = self.send_pages()
            total_time += time
            if total_time >= self.time_limit:
                if not self.fm:
                    print('minimal downtime could not be achieved (migration cancelled)')
                    return total_time, -1
                else:
                    print('minimal downtime could not be achieved (migration completed anyway)')
                    break
        downtime = self.memory_left / self.connection.rand_transfer_rate() + self.connection.lt
        total_time += downtime
        return total_time, downtime
