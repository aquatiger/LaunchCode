"""
Create a list containing 100 random integers between 0 and 1000
(use iteration, append, and the random module).
Write a function called average that will take the list as a parameter and return the average.

"""

import random

listing = []

for i in range(100):
    listing.append(random.randint(0, 1000))
print(listing)


def average():
    sum = 0
    for i in listing:
        sum += i
        result = sum / len(listing)
    print(len(listing))
    print(result)

average()
