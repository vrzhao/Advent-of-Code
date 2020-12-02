# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import time

start = time.time()


f = open("input.txt", "r")

database = []

for row in f:
    database.append(row.strip('\n').split(' '))


f.close()


valid1 = 0
valid2 = 0

for data in database:
    password = data[2]
    letter = data[1][0]
    policy = data[0].split('-')
    if password.count(letter) >= int(policy[0]) and password.count(letter) <= int(policy[1]):
        valid1 += 1
    if (password[int(policy[0])-1] == letter) != (password[int(policy[1])-1] != letter):
        valid2 += 1

        
print(valid1)
print(valid2)


end = time.time()
print(end-start)

