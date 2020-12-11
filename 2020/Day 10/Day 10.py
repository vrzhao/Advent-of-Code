# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 23:33:55 2020

@author: coldf
"""

import time

joltage = []

with open("input.txt", "r") as f:
    for row in f:
        joltage.append(int(row.strip('\n')))

joltage.append(0)
joltage.append(max(joltage)+3)
joltage = sorted(joltage)

#print(joltage)

start = time.time()

jolt1 = 0
jolt2 = 0
jolt3 = 0

current = 0

for i in range(0,len(joltage)):
    if current + 1 in joltage:
        jolt1 += 1
        current += 1
    elif current + 2 in joltage:
        jolt2 += 1
        current += 2
    elif current + 3 in joltage:
        jolt3 += 1
        current += 3

print(jolt1 * jolt3)       

end = time.time()
print(end-start)

start = time.time()

break_points = [0]

for i in range(0,len(joltage) - 1):
    if joltage[i+1] - joltage[i] == 3:
        break_points.append(i+1)

#print(break_points)

sections = []

for i in range(0,len(break_points)-1):
    sections.append(joltage[break_points[i]:break_points[i+1]])

#print(sections)

def path(adapter, data):
    
    if(len(data)==1):
        return 1
    
    if adapter == max(data):
        return 1
    
    paths = 0
    
    connection = [x for x in joltage if adapter < x <= adapter + 3]
    for adapters in connection:
        paths += path(adapters,data)
        
    return paths

pathways = []
    
for i in range(0,len(sections)):
    pathways.append(path(sections[i][0],sections[i]))

unique = 1
for i in range(0,len(pathways)):
    unique *= pathways[i]

print(unique)


end = time.time()
print(end-start)




