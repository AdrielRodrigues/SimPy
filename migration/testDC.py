from typing import List

from migration.host import *
import random


def test_dc(host_n: int, vms_per_hosts: int):
    dc = []
    for i in range(host_n):
        vms = []
        for j in range(vms_per_hosts):
            vm = VM(2048, 0.5, 70, False, f'test VM {i}:{j}')
            vms.append(vm)
        dc.append(Host(128*1024, 1024, vms))
    return dc


def massive_mig_trigger(dc: List[Host]):
    miglist = []
    mignum = 0
    for i in range(len(dc)):
        miglist.append([])
        for index, vm in dc[i].VMs.items():
            if 1 == random.randint(0,5):
                miglist[i].append(index)
                mignum += 1

    for i in range(len(miglist)):
        for j in range(len(miglist[i])):
            dc[i].migrate(j, 125)
    print(mignum)
