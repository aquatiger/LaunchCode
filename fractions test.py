"""
Try to return the closest fraction to a float
partially pseudocode

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

frackey = [(i, j) for i in range(0,10) for j in range (1,10)]
print(frackey)

# takes the keys of the dictionary turns it into a list so I can sort it
frackey = list(fractions.keys())
frackey.sort()
print(frackey)

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
        print(ranges)

print(fractions)

for i in range(len(ranges)):
    print(i)
    if divided < ranges[0][2]:
        print("Your number", numerator, "/", denominator, "is approximately 0")
        break
    elif divided > ranges[i][1] and divided < ranges[i][2]:
        print(fractions[frackey[i][0]])
        #print("Your number", numerator, "/", denominator, "is approximately", fractions.get(), " / ", fractions.get())
    elif divided > ranges[-1][2]:
        print("Your number", numerator, "/", denominator, "is approximately 1")
        break
    
    
##    fractions.ranges[b]
##    pseudocode = first value in the tuple of ranges that matches of the key of fractions
##          take the first of the tuple of values
##    pseudocode2 = first value in the tuple of ranges that matches of the key of fractions
##          take the second of the tuple of values
##    print("Your number: ", + numerator + "/" + denominator + "is approximately equal to" pseudocode / pseudocode2)
##

