
import math
from decimal import Decimal

def findHypot(a, b):
    c = math.sqrt((a ** 2) + (b ** 2))
    if c == (round(c)):
        print(round(c))
    else:
        print(round(c, 4))

findHypot(4, 5)
