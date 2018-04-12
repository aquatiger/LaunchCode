
import math

def isPrime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    print(True)

isPrime(21)
