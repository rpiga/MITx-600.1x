# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 00:25:26 2017

@author: Roberto Piga
"""
# Paste your code into this box
# define variables like in the example, below
balance = 999999; annualInterestRate = 0.18
# Expected result Lowest Payment: 90325.03
#balance = 320000; annualInterestRate = 0.2
# Expected result Lowest Payment: 29157.09

# -- start here --
#
initBalance = balance
monthlyInterestRate = annualInterestRate / 12.0
high = (balance * (1 + (monthlyInterestRate))**12) / 12.0
low = balance / 12
f = True

guess = (high + low) / 2.0

while abs(balance) > 0.01:
    balance = initBalance
    for i in range(1,13):
        unpaidBalance = balance - guess
        balance =  unpaidBalance + (monthlyInterestRate * unpaidBalance)

    if balance < -0.01:
        high = guess
    elif balance > 0.01:
        low = guess
        
    guess = (high + low) / 2.0
    
print("Lowest Payment:", round(guess,2))



