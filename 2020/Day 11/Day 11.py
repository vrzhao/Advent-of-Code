# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 05:21:48 2020

@author: coldf
"""

import time
import copy

layout = []

with open("input.txt", "r") as f:
#with open("test.txt", "r") as f:    
#DrAfdch 2418 for part 1 and 2144 for part 2 
    for row in f:
        seats = []
        row = row.strip('\n')
        for space in row:
            seats.append(space)
        layout.append(seats)

max_X = len(layout[0])
max_Y = len(layout)

def check_seat(x,y,layout):
    try:
        if layout[y][x] == '#':
            return 1
        else:
            return 0
    except IndexError:
        return 0

def check_adjacent(x, y,layout):
    list_X = [x-1,x,x+1]
    list_Y = [y-1,y,y+1]
    
    occupied = 0
    
    for x1 in list_X:
        for y1 in list_Y:
            if (x1 == x and y1 == y):
                continue
            occupied += check_seat(x1,y1,layout)
    return occupied

start = time.time()

new_layout = copy.deepcopy(layout)
run = 0

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
            adjacency = check_adjacent(x,y,new_layout)
#            print(new_layout[y][x], adjacency)
            if new_layout[y][x] == 'L' and adjacency == 0:
                temp_layout[y][x] = '#'
#                print(new_layout[y][x], temp_layout[y][x])                
                changes += 1
            elif new_layout[y][x] == '#' and adjacency >= 4:
                temp_layout[y][x] = 'L'
#                print(new_layout[y][x], temp_layout[y][x])                
                changes += 1
            elif new_layout[y][x] == '.':
                continue
            print(new_layout[y][x],adjacency,temp_layout[y][x])

    if(changes == 0):
        break
    new_layout = copy.deepcopy(temp_layout)
    run += 1

    print(run,occupied_seats(temp_layout))


end = time.time()
print(end-start)














