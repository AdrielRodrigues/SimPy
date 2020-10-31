# from migration import testDC
from host import *

dat = []
data = open("graficos2.csv", "w")
data.write(' ,')
for i in range(1, 11):
    data.write(f'{i*10}%, ')
data.write('\n')
for j in range(1,5):
    dtr = j*31.25
    for i in range(1, 11):
        ops = PreCopyMigrationOPS(2048, 6*i, 30, Connection(dtr, 0, 0, 0.17), 100000, False)
        dat.append(ops.migrate()[0])
    data.write(f'{25*j}% da largura de banda, ')
    for a in dat:
        data.write(f'{a}, ')
    data.write('\n')
    dat = []




# dc = testDC.test_dc(30, 50)
# testDC.massive_mig_trigger(dc)
