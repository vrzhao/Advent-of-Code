# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 21:48:14 2020

@author: coldf
"""

import time
import re


color_regex = r'\w+\s\w+\sbag'

database1 = {}

with open("input.txt", "r") as f:
    for row in f:
        instruction = row.split('contain')
        
        container = instruction[0][:-6]
        instruction2 = re.findall(color_regex,instruction[1])
        contained = []
        for bag in instruction2:
            contained.append(bag[:-4])
        database1[container] = contained
        


contains_gold = ['shiny gold']

def contain_gold(color):

    if len(set.intersection(set(contains_gold),set(database1[color]))) > 0:
        return 1
    if 'no other' in database1[color]:
        return 0
    
    contained = 0
    
    for colors in database1[color]:
        if contain_gold(colors) == 1:
            contains_gold.append(colors)
            contained = 1
            break
    
    return contained
        
start = time.time()

count = 0

for key in database1:
    count += contain_gold(key)

print(count)

end = time.time()
print(end-start)

color_regex = r'[0-9]\s\w+\s\w+\sbag'

database2 = {}

with open("input.txt", "r") as f:
    for row in f:
        instruction = row.split('contain')
        
        container = instruction[0][:-6]
        instruction2 = re.findall(color_regex,instruction[1])
        contained = []
        for bag in instruction2:
            contained.append(bag[:-4])
        database2[container] = contained


start = time.time()

def contained_bags(color):
    if 'no other' in database2[color]:
        return 0
    
    contained = 0
    
    for colors in database2[color]:
        contained += int(colors[0]) + int(colors[0]) * contained_bags(colors[2:])
        
    return contained

start = time.time()

print(contained_bags('shiny gold'))

end = time.time()
print(end-start)

