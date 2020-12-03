# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 02:32:53 2020

@author: coldf
"""

import time

start = time.time()


f = open("input.txt", "r")

database = []

for row in f:
    database.append(row.strip('\n'))


f.close()

width = len(database[0])
height = len(database)


def check_route(database, right, down):
    location = [0,0]
    trees_hit = 0
    while(location[0]<height-1):
        location[0] += down
        location[1] += right
        if location[1] > width - 1:
            location[1] -= width
        if (database[location[0]][location[1]]=='#'):
            trees_hit += 1
    return trees_hit

instructions = [[1,1],[3,1],[5,1],[7,1],[1,2]]
results = []

print(check_route(database, 3, 1))
end = time.time()
print(end-start)

start = time.time()

product = 1

for route in instructions:
    product *= check_route(database, route[0], route[1])
    
print(product)

end = time.time()
print(end-start)
