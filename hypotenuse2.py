import math

hours_ =  5
def isRtAngled(a, b, c):
    list = [a, b, c]
    list.sort(key=int)
    x = list[0]
    y = list[1]
    z = list[2]
    if abs((x ** 2) + (y ** 2) - (z ** 2)) < .00001:
        print(True)
    else:
        print(False)

isRtAngled(8, 10, 6)
