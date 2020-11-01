from migrationtools import *
from typing import List


class Process:
    def __init__(self, demand: float):
        self.demand = demand


class VM:
    """
    img_size        - " "
    sys_cpu_use     - cpu use dedicated to system in proportion (0.0 - 1.0)
    time_sensitive  - if the service offered by this vm is time sensitive
    label           - identify the type o service offered by a VM
    """
    def __init__(self, img_size, sys_cpu_use, wr_per_use, time_sensitive=False, label=""):
        self.img_size = img_size
        self.sys_cpu_use = sys_cpu_use
        self.wr_per_use = wr_per_use
        self.time_sensitive = time_sensitive
        self.label = label
        self.total_cpu_use = self.sys_cpu_use
        self.processes = {}
        self.processes_id_counter = 1

    def __str__(self):
        return f'img_size: -{self.img_size} MB-, label:"{self.label}"'

    def add_process(self, process):
        new_cpu_demand = self.total_cpu_use + process.demand
        if not new_cpu_demand <= 1:
            raise Exception("cpu limit")
        self.total_cpu_use = new_cpu_demand
        self.processes[self.processes_id_counter] = {"demand": process.demand, "active": True}
        self.processes_id_counter += 1
        return True

    def remove_process(self, process_id):
        if process_id in self.processes:
            if not self.processes[process_id]["active"]:
                raise Exception("process is not active")
            self.total_cpu_use = self.total_cpu_use - self.processes[process_id]["demand"]
            self.processes.pop(process_id)
        else:
            raise Exception("process do not exist")


class Host:
    """
    cpu_num             - number of cores in the system
    total_memory        - "
    system_memory       - memory consumed by the host system
    virtualization_cost - proportion of cpu lost due to virtualization
    concurrency_cost   - proportion of cpu lost due to core concurrency
    vms                 - list of Virtual machines
    """
    def __init__(self, cpu_num, total_memory, system_memory, virtualization_cost, concurrency_cost, vms: List[VM]):
        self.cpu_num = cpu_num
        self.total_memory = total_memory
        self.virtualization_cost = virtualization_cost
        self.concurrency_cost = concurrency_cost

        self.VMs = []
        for i in range(self.cpu_num):
            self.VMs.append({})
        self.free_mem = self.total_memory - system_memory
        self.vm_id_counter = 0
        for vm in vms:
            self.add_vm(vm, self.vm_id_counter % self.cpu_num)

    def __str__(self):
        vm_num = 0
        core_dscrptn = ''
        for core in self.VMs:
            vm_num += len(core)
            for vm in core.values():
                core_dscrptn += str(vm) + ' | '
            core_dscrptn += '\n'
        dscrptn = f'total system memory:{self.total_memory}\n' \
                  f'available memory:{self.free_mem}\n' \
                  f'number of guest VMs: {vm_num}\n' \
                  f'{core_dscrptn}'
        return dscrptn

    def add_vm(self, vm: VM, cpu_index: int):
        if self.free_mem > vm.img_size:
            self.free_mem -= vm.img_size
            self.VMs[cpu_index][self.vm_id_counter] = vm
            self.vm_id_counter += 1
        else:
            raise Exception('not enough memory available')

    def pop_vm(self, n):
        for core_index in range(len(self.VMs)):
            if n in self.VMs[core_index]:
                self.free_mem += self.VMs[core_index][n].img_size
                self.VMs[core_index].pop(n)
                return True
        return False

    def migrate(self, vm_index, bandwidth):
        cn = MigrationConnection(bandwidth, 10, 0.005)
        for core in self.VMs:
            if vm_index in core:
                vm = core[vm_index]
                mig = PreCopyMigrationOPS(vm.img_size,
                                          vm.total_cpu_use * vm.wr_per_use,
                                          30, cn, 500, not vm.time_sensitive)
                print(mig.migrate())
                self.pop_vm(vm_index)
                return True
        return False
