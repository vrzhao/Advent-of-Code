# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 12:13:29 2019

@author: Vincent Zhao
"""

f = open("input.txt", "r")

#### part 1 #####
#total_fuel = 0
#
#for row in f:
#    total_fuel += int(int(mass) / 3) - 2 


#### part 2 ####
total_fuel = 0

def required(mass):
    fuel = int(mass / 3) - 2 
    if fuel <= 0:
        return 0
    else:
        return fuel + required(fuel)

for row in f:
    total_fuel += required(int(row))



f.close()

print(total_fuel)



