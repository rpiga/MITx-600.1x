# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 22:08:00 2017

@author: Roberto Piga
"""

s = 'azcbobobegghakl'
s = 'abcbcd'

subString = ""
maxString = ""
charval = ""

for char in s:
    if char >= charval:
        subString += char
    elif char < charval:
        if len(subString) > len(maxString):
            maxString = subString
        subString = char

    charval = char

print("Longest substring in alphabetical order is:", maxString)