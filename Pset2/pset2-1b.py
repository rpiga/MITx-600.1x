# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 00:15:20 2017

@author: Roberto Piga

Version 2
iterate (good for test)
"""

balance = a = 3329
annualInterestRate = b = 0.2
monthlyPaymentRate = c = 0.04

for month in range(1,13):
    # calculate unpaid balance as balance minus the minimum payment
    unpaidBalance = balance - (balance * monthlyPaymentRate)
    # add monthly interest to calculate remaining balance
    remainBalance =  unpaidBalance + (annualInterestRate/12.0 * unpaidBalance)
    # balance for the next month is now the remaing balance from previous
    balance = remainBalance
    
print("Remaining balance:",round(balance, 2))