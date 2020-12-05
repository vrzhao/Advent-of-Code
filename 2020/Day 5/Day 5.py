# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 00:34:38 2020

@author: coldf
"""

import time
import math
import re

database = []

f = open("input.txt", "r")

for row in f:
    database.append(row.strip('\n'))
    
f.close()

def BSP(instructions):
    location = [0, 2**len(instructions)-1]
    for instruction in instructions:
        if instruction in ['F','L']:
            location[1] = math.floor(sum(location)/2)
        else:
            location[0] = math.ceil(sum(location)/2)
            
    return location[0]
def calculate_seatID(instructions):
    row = BSP(re.findall("[FB]",instructions))
    column = BSP(re.findall("[LR]",instructions))
    
    return (row*8)+column

# Part 1
start = time.time()

ID_list = []

for boarding_pass in database:
    seatID = calculate_seatID(boarding_pass)
    ID_list.append(seatID)

print(max(ID_list))

end = time.time()
print(end-start)

# Part 2
start = time.time()

for seatID in ID_list:
    if seatID+2 in ID_list and seatID+1 not in ID_list:
        print(seatID+1)
        break

end = time.time()
print(end-start)

















