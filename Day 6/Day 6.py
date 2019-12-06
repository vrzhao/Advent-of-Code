# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 22:01:58 2019

@author: Vincent Zhao
"""

import time

f = open("input.txt", "r")

database = []
map_ = dict()

for row in f:
    data = row.strip().split(')')
    orbitee = data[0]
    orbiter = data[1]
    
    database.append(orbitee)
    database.append(orbiter)
    map_.update({orbiter:orbitee})

objects = set(database)

f.close()

start = time.time()

total_orbits = 0

for object_ in objects:
    pointer = object_
    orbits = 0
    while pointer != 'COM':
        orbits += 1
        pointer = map_.get(pointer)
        
    total_orbits += orbits

print("Part 1:", total_orbits)

end = time.time()

print("Runtime:", end - start, '\n')

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
        
        
        
        
        
        
        
        
        