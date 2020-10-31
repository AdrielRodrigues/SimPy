from migrationtools import *
from typing import List

class Process:
    def __init__(self, demand):
        self.demand = demand


class VM:
    # img_size ""
    # sys_cpu_use - cpu use dedicated to system in proportion (0.0 - 1.0)
    # time_sensitive - if the service offered by this vm is time sensitive
    # label - identify the type o service offered by a VM
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
        return f'img_size:{self.img_size}, label:{self.label}'

    def add_process(self, process):
        new_cpu_demand = self.total_cpu_use+process.demand
        if not new_cpu_demand <= 1:
            raise Exception("cpu limit")
        self.total_cpu_use = new_cpu_demand
        self.processes[self.processes_id_counter] = {"demand":process.demand, "active":True}
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
    def __init__(self, total_memory, system_memory, vms: List[VM]):
        if vms is None:
            vms = []
        self.VMs = {}
        self.total_memory = total_memory
        self.free_mem = self.total_memory - system_memory
        self.vm_id_counter = 0
        for vm in vms:
            self.add_vm(vm)

    def __str__(self):
        return f'total system memory:{self.total_memory}\navailable memory:{self.free_mem}\n' \
               f'number of guest VMs: {len(self.VMs)}'

    def add_vm(self, vm: VM):
        if self.free_mem > vm.img_size:
            self.free_mem -= vm.img_size
            self.VMs[self.vm_id_counter] = vm
            self.vm_id_counter += 1
        else:
            raise Exception('not enough memory available')

    def pop_vm(self, n):
        if n in self.VMs:
            self.free_mem += self.VMs[n].img_size
            self.VMs.pop(n)
        else:
            raise Exception(f'vm {n} does not exist')

    def migrate(self, vm_index, bandwidth):
        cn = Connection(bandwidth, 10, 0.005)
        if vm_index in self.VMs:
            vm = self.VMs[vm_index]
            mig = PreCopyMigrationOPS(vm.img_size,
                                      vm.total_cpu_use * vm.wr_per_use,
                                      30, cn, 500, not vm.time_sensitive)
            print(mig.migrate())
            self.pop_vm(vm_index)
            return True
        else:
            print('invalid vm index')
            return False

    def list_vms(self):
        vms_list = ''
        if self.VMs == {}:
            vms_list = "no vms"
        for vm_index, vm in self.VMs.items():
            vms_list += f'{vm_index}: {vm}\n'
        return vms_list
