#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

EE 381 Project 3 Part 1
Simulation of a Bernoulli R.V.
@author: Daniel Li
ID: 014504891
Date: 2/27/2019

"""
import random

print("Simulation of Bernoulli Random Variable.")
#---------------------------------------------------------------

p = float(input("Enter the probability of success: "))
T = int(input("Enter the number of trials: "))
print('\n')
#---------------------------------------------------------------

for j in range(T):
    r = random.uniform(0,1)
    if r < p: #Bernoulli
        print('1', end=' ') #Format
    else:
        print('0', end=' ')