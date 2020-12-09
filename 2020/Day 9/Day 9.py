# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 04:20:30 2020

@author: coldf
"""

import time

numbers = []

with open("input.txt", "r") as f:
    for row in f:
        numbers.append(row.strip('\n'))

start = time.time()

def check_preamble(numbers,index):
    subset = numbers[index-25:index]
#    print(subset)
    for i in range(0,25):
        if str(int(numbers[index])-int(subset[i])) in subset:
            return False
    return True

weakness = 0

for i in range(25,len(numbers)-1):
    if check_preamble(numbers,i):
        weakness = [i,numbers[i]]
        print(weakness[1])
        break
    
end = time.time()
print(end-start)

start = time.time()

for i in range(0,len(numbers)):
    contiguous = []
    if i == weakness[0]:
        continue
    for j in range(i,len(numbers)):
        contiguous.append(int(numbers[j]))
        if sum(contiguous) >= int(weakness[1]):
            break
#    print(sum(contiguous))
    if sum(contiguous) == int(weakness[1]):
        print(min(contiguous) + max(contiguous))
        break

end = time.time()
print(end-start)















