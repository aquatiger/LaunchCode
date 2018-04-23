"""
Sum up all the negative numbers in a list.

"""

def negativer(xs):
    negative = 0
    for i in xs:
        negative += i
    print(negative)

xs = list(range(-100, 101))

negativer(xs)
