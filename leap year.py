
# calculates leap years

def leapYear(a):
    if a % 400 == 0:
        print(True)
    elif a % 100 == 0:
        print(False)
    elif a % 4 == 0:
        print(True)
    else:
        print(False)

leapYear(1954)
leapYear(2076)
