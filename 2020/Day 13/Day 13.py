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

schedule = []

for bus in inputs[1].split(','):
    if(bus != 'x'):
        schedule.append(int(bus))
        continue
    schedule.append(bus)
        
#print(busIDs)
start = time.time()

wait_time = []

for bus in schedule:
    if (bus != 'x'):
        minutes = bus - (arrival%bus)
        wait_time.append([minutes, minutes*bus])

wait_time = sorted(wait_time)
print(wait_time[0][1])

end = time.time()
print(end-start)

start = time.time()

timestamp = 100000000000009
while(True):
    increment= 1
    flag = True
    for i in range(0,len(schedule)):
        if schedule[i] != 'x': 
            offset = (timestamp + i) % schedule[i]
            if offset != 0:
                flag = False
            else:
                increment *= schedule[i]
    if flag == True:
        break
    timestamp += increment
    
print(timestamp)

end = time.time()
print(end-start)
