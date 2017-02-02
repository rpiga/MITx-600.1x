# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 23:41:54 2017

@author: Roberto Piga

Version 1
Recursive method
Failed because test parser can not call a function
"""
# define starting variables
balance = a = 5000
annualInterestRate = b = 0.18
monthlyPaymentRate = c = 0.02
month = m = 0

def balancer(balance, annualInterestRate, monthlyPaymentRate, month = 0):
    # base case
    # 12th month print remaining balance and exit
    
    if month == 12:
        print("Remaining balance:",round(balance, 2))
        return True
    else:
        # calculate unpaid balance as balance minus the minimum payment
        unpaidBalance = balance - (balance * monthlyPaymentRate)
        # add monthly interest to calculate remaining balance
        remainBalance =  unpaidBalance + (annualInterestRate/12.0 * unpaidBalance)
        
        # loop to the next month
        return balancer(remainBalance, annualInterestRate, monthlyPaymentRate, month + 1)
        

balancer(a, b, c)