# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 21:27:47 2017

@author: Roberto Piga
"""

s = "azcbobobegghakl"

count = 0
for char in s:
    if char in ('a', 'e', 'i', 'o', 'u'):
        count += 1
        
print("Number of vowels:", count)
