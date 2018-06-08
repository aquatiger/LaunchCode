"""
remove punctuation
count words in a file
use dictionary for word count of each word in alphabetical order

"""

import string

gettysburg = open("C:/Users/Roger/Documents/GitHub/LaunchCode/gettysburg.txt", "r")

puncless = ""
for char in gettysburg:
    if char in string.punctuation:
        gettysburg.replace(char, "")
    else:
        puncless += char
print(puncless)

address = []
for line in gettysburg:
    splitted = line.split()
    address += splitted
print(address)
