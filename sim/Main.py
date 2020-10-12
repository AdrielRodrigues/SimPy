import sys
from sim.Simulator import Simulator

# List size: XML seed [-trace] [-verbose] [-failure] [minload maxload step]
args_size = len(sys.argv)
usage = 'Usage: flexgridsim [simulation_file] [seed] [minload maxload step] [-trace] [-verbose] [-failure]'
trace = False
# TODO: Avaliar remover o Verbose
verbose = False
failure = False

if args_size <= 5 or args_size > 9:
    print(usage)
    exit(0)
else:
    simConfigFile = sys.argv[1]
    seed = int(sys.argv[2])
    minload = int(sys.argv[3])
    maxload = int(sys.argv[4])
    step = int(sys.argv[5])

    if 'trace' in sys.argv:
        trace = True
    if 'verbose' in sys.argv:
        verbose = True
    if 'failure' in sys.argv:
        failure = True

    for load in range(minload, maxload + step, step):
        # TODO: Verificar as importações, colocar em pacotes, etc...
        sim = Simulator()
        sim.execute(simConfigFile, trace, verbose, failure, load, seed)