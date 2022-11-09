# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 07:57:16 2022

@author: ronal
"""

total_sum = 0
for i in range(1000):
    if (i%3 == 0 or i%5 == 0):
        total_sum = total_sum+i
print (total_sum)


#Comments about why the coding work 
#To improve readability I left space between numbers, operators, and variables 
#I did specify the range = 1000
#I specify the multiples of 3 and 5 I would like to get within the range = 1000