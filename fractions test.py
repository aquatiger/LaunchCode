"""
Try to return the closest fraction to a float

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

# takes the keys of the dictionary turns it into a list so I can sort it
frackey = list(fractions.keys())
frackey.sort()


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


for i in range(len(ranges)):
    if divided < ranges[0][2]:
        print("Your number", numerator, "/", denominator, "is approximately 0")
        break
    elif divided > ranges[i][1] and divided < ranges[i][2]:
        print("Your number  " + str(numerator) + "/" + str(denominator) + "  is approximately  " + str(fractions[ranges[i][0]][0]) + "/" + str(fractions[ranges[i][0]][1]))
        print("Your number ",  numerator, "/",  denominator, " is approximately ", fractions[ranges[i][0]][0], "/", fractions[ranges[i][0]][1])
    elif divided > ranges[-1][2] and divided <=1:
        print("Your number", numerator, "/", denominator, "is approximately 1")
        break
    elif divided > 1:
        #bigger = 
        pass

