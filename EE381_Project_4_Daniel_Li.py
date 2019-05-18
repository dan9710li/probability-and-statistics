#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EE 381 Project 4
Name: Daniel Li
I.D. #: 014504891
Start Date: 3-25-2019
End Date: 4-10-2019
Project Description: Simulation of binomial distribution with bar chart
Exercise 1: P({x=3})=(5!/(3!)((2!)))(0.7^3)(0.3^2) = .3087
Exercise 2: n = 5, p = 0.7 thus mean is 5(0.7) = 3.5 and standard deviation is sqrt(5 x 0.7 x 0.3) = 1.025

"""

def main():
    
    def parameters():
        p = float(input("Enter the probability of success: "))
        n = int(input("Enter the number of trials: "))
        print("The probability of more than one success can be calculated.")
        y_low = int(input("What step do we start? "))
        y_high = int(input("What step do we stop? "))
        print("\n")
        return p, n, y_low, y_high
    
    def binomial(p, n, y_low, y_high): 
        Y = [] # Binomial trial record
        N = 594829 # Number of repititions of experiment
        b = [0]*(n+1)
        ave = 0 # Accumulator to calculate average
        M = [] # Recording all outcomes to be used to determine average
        import random

        for j in range(N):
            
            # The binomial experiment
            for i in range(n):
                r = random.uniform(0,1)
                if r < p:
                    x = 1 # Bermoulli
                else:     # Random
                    x = 0 # Variable
                Y.append(x)
            outcome = sum(Y) # Values of 0 through n
            b[outcome] = b[outcome] + 1 # probabilities
            M.append(outcome)
            ave = ave + outcome # For determining average
            Y.clear()
        for k in range(n+1):
            b[k] = b[k]/N
            
        prob = 0 # Accumulator
        for k in range(y_low, y_high+1):
            prob = prob + b[k]
        print("The sum of the probabilies from", y_low, "to", y_high, "is", prob, ".")
        
        ave = ave/N
        print("The average is: ", ave, ".")
        
        #Below is the determination of standard deviation
        import math
        m = 0 # Accumulator
        for i in M:
            m = m + (i - ave)**2
        m = m/N
        sigma = math.sqrt(m)
        print("The standard deviation is: ", sigma, ".")
        
        return b
        
    def histogram(n, b):
        import matplotlib.pyplot as pmf
        from matplotlib.ticker import FormatStrFormatter
        w = 1 #width
        a = []
        for i in range(n+1):
            a.append(i)
            
            
        fig,ax=pmf.subplots()    
        ax.yaxis.set_major_formatter(FormatStrFormatter("%.4f"))
            
        pmf.bar(a,b,w,color=['r','g','m','b','y','c'])
        
        pmf.title('Histogram of Binomial pmf', loc = 'right', color = 'b')
        
        pmf.ylabel('Probabilities', color = 'c')
        
        pmf.xlabel('Number of Successes', color = 'r')
        
        for i in range(len(b)):
            print("For R.V. value", i, "the probability is", b[i])
    
    prob, trials, begin, end = parameters()
    y = binomial(prob, trials, begin, end)
    histogram(trials, y)    
    
main()