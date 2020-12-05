# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 03:20:43 2020

@author: coldf
"""
import time
import re

# Part 1
start = time.time()

print("Part 1: ", max([int(re.sub('[BR]','1',re.sub('[FL]','0',row.strip('\n'))),2) for row in open("input.txt", "r")]), "\t Part 2: ", max([seatID+1 for seatID in [int(re.sub('[BR]','1',re.sub('[FL]','0',row.strip('\n'))),2) for row in open("input.txt", "r")] if (seatID+2 in [int(re.sub('[BR]','1',re.sub('[FL]','0',row.strip('\n'))),2) for row in open("input.txt", "r")] and seatID+1 not in [int(re.sub('[BR]','1',re.sub('[FL]','0',row.strip('\n'))),2) for row in open("input.txt", "r")])]))

end = time.time()
print(end-start)

