# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 00:25:48 2020

@author: coldf
"""


import time

from collections import defaultdict

puzzle_input = [12,1,16,3,11,0]


start = time.time()

spoken_index = defaultdict(list)

for num in puzzle_input:
    spoken_index[num].append(puzzle_input.index(num))


next_val = 0

turns = 30000000

for i in range(len(puzzle_input), turns -1):
#    print(last)
    if next_val in spoken_index.keys():
        spoken_index[next_val].append(i)
        next_val = i-spoken_index[next_val][-2]
    else:
        spoken_index[next_val].append(i)
        next_val = 0
    if i == 2018:
        print(next_val)

print(next_val)


end = time.time()
print(end-start)
