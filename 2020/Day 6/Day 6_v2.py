# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 01:00:27 2020

@author: coldf
"""

import time

start = time.time()

print([sum(u) for u in zip(*[(len([set.union(*[set(y) for y in z])][0]),len([set.intersection(*[set(y) for y in z])][0])) for z in [x.split('\n') for x in ("".join([x for x in open("input.txt", "r")])).split('\n\n')]])])

end = time.time()
print(end-start)



