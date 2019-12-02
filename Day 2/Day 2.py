# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 22:03:53 2019

@author: Vincent Zhao
"""

import re

f = open("input.txt", "r")
string = f.read()

x = re.sub('\n','',string)

str_data = x.split(',')
dataset = [int(x) for x in str_data]

def opcodes(data, noun, verb):   
    data[1] = noun
    data[2] = verb    
    for i in range(0,len(data), 4):
        if data[i] == 1:
            data[data[i+3]] = data[data[i+1]] + data[data[i+2]]
        elif data[i] == 2:
            data[data[i+3]] = data[data[i+1]] * data[data[i+2]]
        else:
            break
    return data[0]

#### part 1 ####

print(opcodes(dataset.copy(),12,2))

#### part 2 ####

target = 19690720

for noun in range(0,100,1):
    for verb in range(0,100,1):
        if opcodes(dataset.copy(),noun,verb) == target:
            print(100 * noun + verb)            
            noun, verb = 100, 100            