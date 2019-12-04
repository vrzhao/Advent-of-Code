# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 22:07:24 2019

@author: Vincent Zhao
"""


#possible = 0
#
#
#for i in range (min_input + 1, max_input):
#    password = str(i)
#    
#    pair = False
#    decreasing = True
#    l_group = False
#    
#    for j in range(5):
#        if int(password[j]) == int(password[j+1]):
#            pair = True                
#            continue
#        elif int(password[j]) < int(password[j+1]):
#            continue
#        else:
#            decreasing = False
#            break
#
#    if pair & decreasing:
#        possible += 1
#

def run(min_input, max_input):   
    possible = 0
    possible2 = 0
    
    for i in range (min_input + 1, max_input):
        password = str(i)
        
    #    pair = False
        pairs = dict()
        decreasing = True
        
        for j in range(len(password) - 1):
            X = int(password[j])
            Y = int(password[j+1])
            if X == Y :
                if X not in pairs.keys():
                    pairs.update({X: True})
                elif X in pairs.keys():
                    pairs.update({X: False})
                continue
            elif X < Y:
                continue
            else:
                decreasing = False
                break
            
        if decreasing:
            if len(pairs) > 0:
                possible += 1
            for couple in pairs:
                if pairs.get(couple):
                    possible2 += 1
                    break
            
    
    print("Part 1:", possible)
        
    print("Part 2:", possible2)

        

min_num = 264360
max_num = 746325

run(min_num, max_num)
        
        
        
        
        