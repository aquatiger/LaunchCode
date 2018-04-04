def mySqrt(n):
    oldguess = 1/2*n
    newguess = (1/2) * (oldguess + (n/oldguess))
    while newguess != oldguess:     #this I googled, probably would not have thought of myself
        oldguess = newguess
        newguess = (1/2) * (oldguess + (n/oldguess))
        print(newguess)

print(mySqrt(5))
