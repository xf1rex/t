#!/usr/bin/python

import pandas as pd
import numpy as np
import time
    
col_1 = pd.read_csv('/home/mininet/Scrivania/CSV/vlan_interfaccia1_DOS.csv', sep=';', usecols=[7], skiprows=[0])
col_2 = pd.read_csv('/home/mininet/Scrivania/CSV/vlan_interfaccia1_DOS.csv', sep=';', usecols=[8], skiprows=[0])

arr_1 = col_1.values
arr_2 = col_2.values

i = 0

h1.cmd('./ITGRecv &')
h2.cmd('./ITGRecv &')
time.sleep(10)

while i < arr_1.size:
    n = int(arr_1[i])
    avg = n / 300
    print 'Exec ITGSend on H1 with avg equal to ' , avg
    com = './ITGSend -a 10.0.0.2 -b 160 -C ' + str(avg) + ' -t 300000 &'
    print(com)
    h1.cmd(com)
    n = int(arr_2[i])
    avg = n / 300
    print 'Exec ITGSend on H2 with avg equal to ' , avg
    com = './ITGSend -a 10.0.0.1 -b 160 -C ' + str(avg) + ' -t 300000 &'
    print(com)
    h2.cmd(com)

    i = i+1
    time.sleep(300)
