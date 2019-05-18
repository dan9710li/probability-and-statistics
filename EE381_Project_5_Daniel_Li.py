#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EE 381 Project 5
Name: Daniel Li
I.D. #: 014504891
Start Date: 4-22-2019
End Date: 4-22-2019
Project Description: Simulation of binomial distribution with bar chart
"""
#Hypothesis: H0: p = 1/2 H1: p > 1/2

import matplotlib.pyplot as power

p = [0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 1.00]

#The beta values corresponding the p values
Beta = [0.8923, 0.7911, 0.6448, 0.4658, 0.2831, 0.1322, 0.0423, 0.0064, 0.0002, 0.0000]

b = []
for i in Beta:
    b.append(1 - i)
    
power.plot(p,b)
power.xlabel("P Values")
power.ylabel("1 - P")
power.title("Power curve")