"""
Write a Python function that will take a the list of 100 random integers between 0 and 1000
and return the maximum value.
(Note: there is a builtin function named max but pretend you cannot use it.)

"""

import random

aList = []
sum = 0

for i in range(100):
    aList.append(random.randint(0, 1000))


print(aList)
for i in aList:    
    if i  % 2 == 1:
        sum += i
    elif i % 2 == 0:
        print(sum)
        break
