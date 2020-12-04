# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 03:12:33 2020

@author: coldf
"""

import time

start = time.time()


f = open("input.txt", "r")

database = []
passport = {}

for row in f:
    if row == '\n':
        database.append(passport)
        passport = {}

        continue
    
    deliminated = row.strip('\n').split(' ')
    for field in deliminated:
        passport[field[0:3]] = field[4:]


f.close()

required_fields = set(['byr','iyr','eyr','hgt','hcl','ecl','pid'])
valid_colors = set(list(map(chr, range(ord('a'), ord('f')+1))) + list(map(str, range(0, 10))))
valid_passports1 = 0
valid_passports2 = 0

for data in database:
    if required_fields.issubset(set(data)):
        valid_passports1 += 1
        
        if int(data['byr']) < 1920 or int(data['byr']) > 2002:
            continue
        if int(data['iyr']) < 2010 or int(data['iyr']) > 2020:
            continue
        if int(data['eyr']) < 2020 or int(data['eyr']) > 2030:
            continue
        if data['hgt'][-2:] not in ['in','cm']:
            continue
        if data['hgt'][-2:] == 'cm':
            if int(data['hgt'][:-2]) < 150 or int(data['hgt'][:-2]) > 193:
                continue
        if data['hgt'][-2:] == 'in':
            if int(data['hgt'][:-2]) < 59 or int(data['hgt'][:-2]) > 76:
                continue
        if data['hcl'][0] != '#' or len(data['hcl'][1:]) != 6 or not set(data['hcl'][1:]).issubset(valid_colors):
            continue
        if data['ecl'] not in ['amb','blu','brn','gry','grn','hzl','oth']:
            continue
        if len(data['pid']) != 9 or not (data['pid'].isnumeric()):
            continue
        valid_passports2 += 1
        

print(valid_passports1)
print(valid_passports2)

end = time.time()
print(end-start)








