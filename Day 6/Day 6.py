# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 22:01:58 2019

@author: Vincent Zhao
"""

import time

f = open("input.txt", "r")

map_ = dict()

for row in f:
    orbitee, orbiter = row.strip().split(')')
    map_.update({orbiter:orbitee})

f.close()

### Part 1 ###
start = time.time()

total_orbits = 0

for object_ in map_:
    pointer = object_
    orbits = 0
    while pointer != 'COM':
        total_orbits += 1
        pointer = map_.get(pointer)
        
print("Part 1:", total_orbits)

end = time.time()

print("Runtime:", end - start, '\n')

### Part 2 ###
start = time.time()

you_chain = []
san_chain = []
you_pointer = 'YOU'
san_pointer = 'SAN'

while True:
    you_pointer = map_.get(you_pointer)
    san_pointer = map_.get(san_pointer)
    
    you_chain.append(you_pointer)
    san_chain.append(san_pointer)

    if you_pointer in san_chain:
        print("Part 2:", you_chain.index(you_pointer) + san_chain.index(you_pointer))
        break
    
    if san_pointer in you_chain:
        print("Part 2:", you_chain.index(san_pointer) + san_chain.index(san_pointer))
        break

end = time.time()

print("Runtime:", end - start, '\n')
        
        
        
        
        
        
        
        
        