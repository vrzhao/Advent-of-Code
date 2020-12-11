# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 05:21:48 2020

@author: coldf
"""

import time
import copy

layout = []

with open("input.txt", "r") as f:
    for row in f:
        seats = []
        row = row.strip('\n')
        for space in row:
            seats.append(space)
        layout.append(seats)

max_X = len(layout[0])
max_Y = len(layout)
#print(max_X*max_Y)
def check_seat(x,y):
    try:
        if new_layout[y][x] == '#':
            return 1
        else:
            return 0
    except IndexError:
        return 0

def check_adjacent(x, y):
    list_X = [x-1,x,x+1]
    list_Y = [y-1,y,y+1]
    
    occupied = 0
    
    for x1 in list_X:
        for y1 in list_Y:
            if (x1 == x and y1 == y):
                continue
            occupied += check_seat(x1,y1)
    return occupied

start = time.time()

new_layout = copy.deepcopy(layout)
run = 1

#def change_seats(layout):
#    pass
def occupied_seats(layout):
    occupied = 0

    for row in layout:
        occupied += row.count('#')
    return occupied

while(True):
    temp_layout = copy.deepcopy(new_layout)
    
    changes = 0
    
    for y in range(0,max_Y):
        for x in range(0,max_X):
#            print(x,y)
            adjacency = check_adjacent(x,y)
            if new_layout[y][x] == 'L' and adjacency == 0:
                temp_layout[y][x] = '#'
                changes += 1
            elif new_layout[y][x] == '#' and adjacency >= 4:
                temp_layout[y][x] = 'L'
                changes += 1
    if(changes == 0):
        break
    new_layout = copy.deepcopy(temp_layout)
    run += 1

    print(run,occupied_seats(new_layout))


end = time.time()
print(end-start)














