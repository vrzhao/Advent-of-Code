# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 03:02:31 2020

@author: coldf
"""

import time
import re

# Part 1
start = time.time()

f = open("input.txt", "r")

ID_list = [(int(re.sub('[BR]','1',re.sub('[FL]','0',row.strip('\n'))),2)) for row in f]

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










