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
                fractions.append((x, i, j))"""
Try to return the closest fraction to a float

"""
numerator = int(input("Please enter the top or first number you want to divide: "))
denominator = int(input("Please enter the bottom or second number you want to divide: "))
divided = numerator / denominator

fractions = {}

# this generates a dictionary with values in a list of the numerator and the denominator
for i in range(0, 10):
    for j in range(1, 10):
        if i < j:
            x = i/j
            if x not in fractions:
                fractions[x] = list((i, j))

# takes the keys of the dictionary turns it into a list so I can sort it
frackey = list(fractions.keys())
frackey.sort()


ranges = []

for i in range(len(frackey)):
    try:
        a = frackey[i-1]
        b = frackey[i] # b is the same as one of the keys in fractions
        c = frackey[i+1]
        y = (b - ((b-a)/2)) # takes the previous float, divides by 2 and subtracts from i
        z = ((c-b)/2) + b    # takes the next float, divides by 2 and adds to i
        ranges.append((b, y, z))
    except IndexError: # needed to put this in because c is out of range otherwise
        y = (b - ((b-a)/2))
        z = ((1-b)/2) + b
        ranges.append((b, y, z))


for i in range(len(ranges)):
    if divided < ranges[0][2]:
        print("Your number", numerator, "/", denominator, "is approximately 0")
        break
    elif divided > ranges[i][1] and divided < ranges[i][2]:
        print("Your number  " + str(numerator) + "/" + str(denominator) + "  is approximately  " + str(fractions[ranges[i][0]][0]) + "/" + str(fractions[ranges[i][0]][1]))
        print("Your number ",  numerator, "/",  denominator, " is approximately ", fractions[ranges[i][0]][0], "/", fractions[ranges[i][0]][1])
    elif divided > ranges[-1][2]:
        print("Your number", numerator, "/", denominator, "is approximately 1")
        break


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

