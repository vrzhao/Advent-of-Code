# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 21:57:21 2019

@author: Vincent Zhao
"""
import time

f = open("input.txt", "r")

wire_1 = f.readline().strip().split(',')
wire_2 = f.readline().strip().split(',')
#
#data_1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
#data_2 = "U62,R66,U55,R34,D71,R55,D58,R83"
#wire_1 = data_1.split(',')
#wire_2 = data_2.split(',')


def run(instructions):
    path = []
    current_pos = (0,0)
    
    for instruct in instructions:
        direction = instruct[0]
        distance = int(instruct[1:])
        
        if direction == 'U':
            for i in range(1,distance + 1):
                path.append((current_pos[0],current_pos[1] + i))
            current_pos = (current_pos[0],current_pos[1] + distance)
            
        if direction == 'D':
            for i in range(1,distance + 1):
                path.append((current_pos[0],current_pos[1] - i))
            current_pos = (current_pos[0],current_pos[1] - distance)    
            
        if direction == 'L':
            for i in range(1,distance + 1):
                path.append((current_pos[0] - i,current_pos[1]))
            current_pos = (current_pos[0] - distance,current_pos[1])    
            
        if direction == 'R':
            for i in range(1,distance + 1):
                path.append((current_pos[0] + i,current_pos[1]))
            current_pos = (current_pos[0] + distance,current_pos[1])
            
    return path

start = time.time()
        
wire_1_path = run(wire_1)
wire_2_path = run(wire_2)

intersections = list(set(wire_1_path) & set(wire_2_path)) 

distances = []

for inter in intersections:
    distances.append(abs(inter[0]) + abs(inter[1]))


print("Part 1:", min(distances))

end1 = time.time()
print(end1-start)

steps = []

for inter in intersections:
    steps.append(wire_1_path.index(inter) + wire_2_path.index(inter) + 2)


print("Part 2:", min(steps))

end2 = time.time()
print((end2-start)-(end1-start))























