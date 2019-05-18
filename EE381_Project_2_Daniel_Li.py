#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 14:05:46 2019
@author: danielli1
#EE 381 Spring 2019 Project 2
Exercise 3
#Name: Daniel Li
#ID: 014504891
#Due Date: 02/20/2019
"""

M = 8601 # Multiplier
A = 4857 # Adder
N = 10000 # Norm
import time
import math

#-------------------------------------------------------------
#Exercise 3 Die

S = time.clock()

for i in range(25):
    S = (S * M + A) % N
    r = S / float(N)
    die = math.floor(r*6+1)
    print(die)
    
#-------------------------------------------------------------
#Exercise 3 Coin

S = time.clock()

for i in range(25):
    S = (S * M + A) % N
    r = S / float(N)
    coin = math.floor(2*r)
    if coin == 0:
        print("Head")
    else:
        print("Tail")

#-------------------------------------------------------------
#using simulation to solve probability problem
#The random number generator will generate the cans
#The three balls in the list will be assigned numbers
#This experiment can be repeated many times
#The ratio of success of total runs will give an aprox answer
#3 Balls in 5 cans

S = time.process_time()
ball = [0, 0, 0] #No balls in the cans.
Sum = 0 #Accumulator
Trials = 5555 # Number of times experiment is repeated

#---------------------------------------
for j in range(Trials):

#---------------------------------------
    for i in range(3):
        S = (S * M + A) % N
        r = S / N
        can_number = math.floor(r * 5 + 1)
        ball[i] = can_number
    if (ball[0] != ball[1] and \
    (ball[1] != ball[2]) and \
    (ball[0] != ball[2])):
        Sum = Sum + 1 #Counting Successes.
    
    
p = Sum / Trials
print("The probability of three balls in different cans is: " ,p, ".")
