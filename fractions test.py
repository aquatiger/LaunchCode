"""
Try to return the closest fraction to a float
partially pseudocode

"""
numerator = int(input("Please enter the top or first number you want to divide: "))
denominator = int(input("Please enter the bottom or second number you want to divide: "))
divided = numerator / denominator

fractions = {}

for i in range(0, 10):
    for j in range(1, 10):
        if i < j:
            x = i/j
            if x not in fractions:
                fractions[x] = (i, j)
                
print(fractions)
frackey = list(fractions.keys())
frackey.sort()
print(frackey)

ranges = []

for i in range(len(frackey)):
    a = frackey[i-1]
    b = frackey[i] # b is the same as one of the keys in fractions
    c = frackey[i+1]

    y = (b - ((b-a)/2))
    z = ((c-b)/2) + b
    ranges.append((b, y, z))
    print(ranges)

##if divided > y and divided < z:
##    fractions.ranges[b]
##    pseudocode = first value in the tuple of ranges that matches of the key of fractions
##          take the first of the tuple of values
##    pseudocode2 = first value in the tuple of ranges that matches of the key of fractions
##          take the second of the tuple of values
##    print("Your number: ", + numerator + "/" + denominator + "is approximately equal to" pseudocode / pseudocode2)
##

