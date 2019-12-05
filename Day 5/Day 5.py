# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 15:09:09 2019

@author: Vincent Zhao
"""

import time

f = open("input.txt", "r")
string = f.read().strip()

str_data = string.split(',')
dataset = [int(x) for x in str_data]
f.close()


def positional(data, address):
    return data[data[address]]
    
def immediate(data,address):
    return data[address]

def values(data, mode, address):
    if mode[0] == 0:
        value1 = positional(data,address+1)
    else:
        value1 = immediate(data,address+1)
    
    if mode[1] == 0:
        value2 = positional(data,address+2)
    else:
        value2 = immediate(data,address+2)  
    
    return value1,value2

def add(data, mode, address):
    value1,value2 = values(data,mode,address)
        
    value3 = value1 + value2

    data[data[address+3]] = value3


def mult(data, mode, address):
    value1,value2 = values(data,mode,address)
    
    value3 = value1 * value2
    
    data[data[address+3]] = value3

def input_(data, number, address):
    data[data[address+1]] = number
    
def output(data, mode, address):
    if mode[0] == 0:
        value = positional(data,address+1)
    else:
        value = immediate(data,address+1)
        
    print("Output:",value)

def jump_if_true(data, mode, address):
    value1,value2 = values(data,mode,address)
    
    if value1 != 0:
        return value2
    else:
        return -1
    
def jump_if_false(data, mode, address):
    value1,value2 = values(data,mode,address)
    
    if value1 == 0:
        return value2
    else:
        return -1
    
def less_than(data, mode, address):
    value1,value2 = values(data,mode,address)
    
    if value1 < value2:
        value3 = 1
    else:
        value3 = 0
    
    data[data[address+3]] = value3
    
def equals(data, mode, address):
    value1,value2 = values(data,mode,address)

    if value1 == value2:
        value3 = 1
    else:
        value3 = 0
    
    data[data[address+3]] = value3

def modes(instruction):
    return [(instruction // 100) % 10, instruction // 1000]
    
def opcodes(data, num):
    i = 0
    
    while(i < len(data)):
        instruction = data[i]
        opcode = instruction % 100
        mode = modes(instruction)
        step = {1: 4, 2: 4, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4, 99:1}[opcode]
        
        if opcode == 1:
            add(data,mode,i)
            
        elif opcode == 2:
            mult(data,mode,i)
            
        elif opcode == 3:
            input_(data,num,i)
            
        elif opcode == 4:
            output(data,mode,i)
            
        elif opcode == 5:
            jump = jump_if_true(data,mode,i)
            
            if jump != -1:
                i = jump
                continue
                
        elif opcode == 6:
            jump = jump_if_false(data,mode,i)
            
            if jump != -1:
                i = jump
                continue
                
        elif opcode == 7:
            less_than(data,mode,i)    
            
        elif opcode == 8:
            equals(data,mode,i)
            
        else:
            break
        
        i += step
        

print("#### part 1 ####")
start = time.time()
input_num = 1
opcodes(dataset.copy(),input_num)
end = time.time()
print("Runtime:", end - start, '\n')

print("#### part 2 ####")
start = time.time()
input_num = 5
opcodes(dataset.copy(),input_num)
end = time.time()
print("Runtime:", end - start)



