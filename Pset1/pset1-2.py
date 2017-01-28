# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 21:38:57 2017

@author: Roberto Piga
"""
s = 'azcbobobegghakl'
pattern = "bob"

count = 0
index = 0

while index < len(s):
    temp = s[index:len(pattern) + index]
    if temp == pattern:
        count += 1
    index += 1

print("Number of times bob occurs is:", count)