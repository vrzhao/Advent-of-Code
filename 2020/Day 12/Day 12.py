# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 05:08:57 2020

@author: coldf
"""

import time

directions = []

with open("input.txt", "r") as f:
    for row in f:
        row = row.split('\n\n')[0].strip('\n')
        instruction = [row[0],int(row[1:])]
        directions.append(instruction)
        

facing = 90
compass = ['N','E','S','W']
X = 0
Y = 0

def move(direction, magnitude):
    global X
    global Y
    if direction == 'N':
        Y += magnitude
    if direction == 'E':
        X += magnitude
    if direction == 'S':
        Y -= magnitude
    if direction == 'W':
        X -= magnitude

def turn(direction, magnitude):
    global facing
    if direction == 'L':
        facing += (360 - magnitude) 
        facing = facing % 360
    if direction == 'R':
        facing += magnitude 
        facing = facing % 360

start = time.time()

for line in directions:
    direction = line[0]
    magnitude = line[1]
    if direction in ['L','R']:
        turn(direction, magnitude)
    if direction in ['N','E','S','W']:
        move(direction, magnitude)
    if direction == 'F':
        move(compass[int(facing/90)], magnitude)
    

print(abs(X) + abs(Y))

end = time.time()
print(end-start)

X = 0
Y = 0

def move_wp(direction, magnitude):
    global waypoint
    if direction == 'N':
        waypoint[1] += magnitude
    if direction == 'E':
        waypoint[0] += magnitude
    if direction == 'S':
        waypoint[1] -= magnitude
    if direction == 'W':
        waypoint[0] -= magnitude

def adjust_wp():
    global waypoint
    x = waypoint[0]
    y = waypoint[1]
    waypoint = [y,-x]

def turn_wp(direction, magnitude):
    turns = 0
    if direction == 'L':
        turns = (360-magnitude)/90
    if direction == 'R':
        turns = magnitude/90
        
    for i in range(0,int(turns)):
        adjust_wp()

start = time.time()

waypoint = [10,1]

for line in directions:
    direction = line[0]
    magnitude = line[1]
    if direction in ['L','R']:
        turn_wp(direction, magnitude)
    if direction in ['N','E','S','W']:
        move_wp(direction, magnitude)
    if direction == 'F':
        X += waypoint[0]*magnitude
        Y += waypoint[1]*magnitude


print(abs(X) + abs(Y))

end = time.time()
print(end-start)










