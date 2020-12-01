# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 02:38:56 2019

@author: Vincent Zhao
"""
import time

def orbc(orbit, planet):
    if planet in orbit['COM']:
        return 1
    else:
        for key in orbit.keys():
            if planet in orbit[key]:
                return 1 + orbc(orbit, key)

f = open("input.txt", 'r')

orbits = {}

for line in f:
    if line == "<>":
        break
    line = line.strip()
    a,b = line.split(')')
    orbits.setdefault(a,[]).append(b)
    
start = time.time()

count = 0

for value in orbits.values():
    for j in range(len(value)):
        count += orbc(orbits,value[j])

print(count)
end = time.time()

print("Runtime:", end - start, '\n')

f.close()