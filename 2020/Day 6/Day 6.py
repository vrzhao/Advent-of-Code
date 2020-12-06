# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 00:24:55 2020

@author: coldf
"""

import time

start = time.time()

group = []

part1 = 0
part2 = 0

with open("input.txt", "r") as f:
    for row in f:
        if row == '\n':
            if len(group) != 0:
                part1 += len(set.union(*group))
                part2 += len(set.intersection(*group))
            group = []
            continue
        
        group.append(set(list(row.strip('\n'))))
        person = []

print(part1)
print(part2)

end = time.time()
print(end-start)



