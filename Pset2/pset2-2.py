# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 00:25:26 2017

@author: Roberto Piga
"""
# Paste your code into this box
# define variables like in the example, below
balance = 3329; annualInterestRate = 0.2

minimumFixed = 0
f = True
initialBalance = balance

while balance > 0:
    balance = initialBalance
    minimumFixed += 10
    
    for month in range(1,13):
        unpaidBalance = balance - minimumFixed
        balance =  unpaidBalance + round(annualInterestRate/12.0 * unpaidBalance)

print("Lowest Payment:", round(minimumFixed))


