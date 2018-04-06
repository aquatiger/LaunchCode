# calculates the date of Easter

year = int(input("Please enter a year between 1900 and 2099 to determine the date of Easter: "))

a = year % 19
b = year % 4
c = year % 7
d = (19 * a + 24) % 30
e = (2 * b + 4 * c + 6 * d + 5) % 7
easter = 22 + d + e

if year != 1954 and year != 1981 and year != 2049 and year != 2076:
    if easter <32:
        print("March", easter)
    else:
        print("April", (easter - 31))

if year == 1954 or year == 1981 or year == 2049 or year == 2076:
    easterSpecial = easter + 7
    print("May", (easterSpecial - 61))
