#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

EE 381 Project 3 Part 2
Simulation of Markov Chain
@author: Daniel Li
ID: 014504891
Date: 2/27/2019


"""

import random
L = [] #Record position of particle
S = random.randint(0, 1) #Initial location of particle
L.append(S)

#Prompt inputting Bermoulli parameters
p = float(input("Enter the probability of going from 0 to 1. "))
q = float(input("Enter the probability of going from 1 to 0. "))
#-----------------------------------------------------------------
for i in range(25):
    r = random.uniform(0, 1)
    if S == 0 and r < p:    #Markov
        S = 1               #Markov
    elif S == 1 and r < q:  #Markov
        S = 0
    L.append(S)
#-----------------------------------------------------------------
#Output
for i in range(25):
    print(L[i], end = ' ')
    if i % 10 == 9:
        print()
