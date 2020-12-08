# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 23:47:45 2020

@author: coldf
"""

import time
import copy

code = []

with open("input.txt", "r") as f:
    for row in f:
        code.append(row.strip('\n').split(' '))

#print(code)

accumulator = 0
index = 0
lines_run = []

start = time.time()

while (index < len(code)):
    if index in lines_run:
        print(accumulator)
        break
    lines_run.append(index)
    line = code[index]
    cmd = line[0]
    amt = line[1]
    if cmd == 'acc':
        accumulator += int(amt)
        index += 1
        continue
    if cmd == 'jmp':
        index += int(amt);
        continue
    if cmd == 'nop':
        index += 1
        continue
    
end = time.time()
print(end-start)
#

start = time.time()

def run_code(codes):  
    index = 0
    accumulator = 0
    lines_run = []
    while (index < len(codes)):
        if index in lines_run:
#            print(index, accumulator)
            return None
        lines_run.append(index)
        line = codes[index]
        cmd = line[0]
        amt = line[1]
        if cmd == 'acc':
            accumulator += int(amt)
            index += 1
            continue
        if cmd == 'jmp':
            index += int(amt);
            continue
        if cmd == 'nop':
            index += 1
            continue
    
    return accumulator

for i in range(0,len(code)):
#    print(i)
    fixed_code = copy.deepcopy(code)
#    print(fixed_code[i][0])
    if fixed_code[i][0] == 'jmp':
        fixed_code[i][0] = 'nop'
    elif fixed_code[i][0] == 'nop':
        fixed_code[i][0] = 'jmp'
#    print(code[i][0], fixed_code[i][0])
    x = run_code(fixed_code)
    if x != None:
        print(x)

end = time.time()
print(end-start)













