# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 00:34:38 2020

@author: coldf
"""

import time
import math
import re


def BSP(instructions):
    location = [0, 2**len(instructions)-1]
    for instruction in instructions:
        if instruction in ['F','L']:
            location[1] = math.floor(sum(location)/2)
        else:
            location[0] = math.ceil(sum(location)/2)
            
    return location[0]
def calculate_seatID(instructions):
    row_instruction = re.findall("[FB]",instructions)
    column_instruction = re.findall("[LR]",instructions)
    row = BSP(row_instruction)
    column = BSP(column_instruction)
    
    return (row*(2**len(column_instruction)))+column

# Part 1
start = time.time()

f = open("input.txt", "r")

ID_list = []

for row in f:
    seatID = calculate_seatID(row.strip('\n'))
    ID_list.append(seatID)

f.close()

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

















