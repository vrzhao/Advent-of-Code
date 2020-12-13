# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 00:07:26 2020

@author: coldf
"""

import time

inputs = []

with open("input.txt", "r") as f:
    for row in f:
        row = row.strip('\n')
        inputs.append(row)

arrival = int(inputs[0])
#print(inputs)

busIDs = []

for bus in inputs[1].split(','):
    if (bus != 'x'):
        busIDs.append(int(bus))
        
#print(busIDs)

for bus in busIDs:
    minutes = bus - (arrival%bus)
    print(minutes, bus, minutes*bus)

schedule = inputs[1].split(',')

timestamp = 100000000000009
while(True):
#    print(timestamp)
    increment= 1
    flag = True
    for i in range(0,len(schedule)):
        if schedule[i] != 'x':
            offset = (timestamp + i) % int(schedule[i])
            if offset != 0:
                flag = False
            else:
                increment *= int(schedule[i])
    if flag == True:
        break
    timestamp += increment
    
print(timestamp)