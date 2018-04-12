
import math
from decimal import Decimal

def findHypot(a, b):
    c = math.sqrt((a ** 2) + (b ** 2))
    if c == (round(c)):
        return round(c)
    else:
        return round(c, 4)

findHypot(3, 4)
