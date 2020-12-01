# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 04:18:41 2020

@author: coldf
"""
import time

start = time.time()

f = open("input.txt", "r")

numbers = []

for row in f:
    numbers.append(int(row))

f.close()

size = len(numbers)

val = 0

for i in range(0,size):
    val = 2020-numbers[i]
    if val in numbers:
        print(numbers[i]*val)
        break

end1 = time.time()
print(end1-start)

for i in range(0,size):
    for j in range(i+1,size):
        val = 2020-numbers[i]-numbers[j]
        if val in numbers:
            print(numbers[i]*numbers[j]*val)
            val = 0
            break
    if val == 0:
        break


end2 = time.time()
print((end2-start)-(end1-start))
