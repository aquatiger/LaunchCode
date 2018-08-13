"""
Try to return the closest fraction to a float
partially pseudocode

"""

import math
#import numpy as numpy

fractions = [(0, 0, 0)]

for i in range(1, 10):
    for j in range(1, 10):
        if i < j:
            x = i/j
            if x not in fractions:
                fractions.append((x, i, j))
    sortedFrac =  sorted(fractions)

print(sortedFrac)
noDupFrac = [(0,0,0)]

for i in range(len(sortedFrac)):
    try:
        if sortedFrac[i][0] == sortedFrac[i-1][0]: # so if the float equals the previous float
            sortedFrac.remove(sortedFrac[i][0])           # remove the second float
        else:
            sortedFrac.append(sortedFrac[i][0])
    except ValueError:
        continue

print(noDupFrac)
"""
The previous for loop works except for the fact it removes all the ones that are equal,
not just the duplicates.
"""
    
"""
for the previous line got TypeError: integer argument expected, got float

for previous line using remove instead of pop got ValueError: list.remove(x): x not in list

"""
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

