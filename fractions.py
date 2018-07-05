"""
Try to return the closest fraction to a float
partially pseudocode

"""

import math
import numpy as numpy

fractions = [(0, 0, 0)]

for i in range(1, 10):
    for j in range(1, 10):
        if i < j:
            x = i/j
            fractions.append((x, i, j))
    sortedFrac =  sorted(fractions)

print(sortedFrac)

##newFrac = []
##
##for i in range(len(fractions)):
##    r = (fractions[i + 1][0])
##    print(r, "r")
##    a = (fractions[i + 1][0]) / j
##    print(a , "a")
##    b = (a - (fractions[i][0] / j)) / 2
##    print(b , "b")
##    c = a - b
##    print(c , "c")
##         
##
##if something > a and something < b:
##    return "approximately equal to" i / j
##

