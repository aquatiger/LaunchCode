"""
remove punctuation (done)
count words in a file (done)
find length of longest word
use dictionary for word count of each word in alphabetical order (done)

"""

import string

gettysburg = open("C:/Users/Roger/Documents/GitHub/LaunchCode/gettysburg.txt", "r")

puncless = ""
for char in gettysburg.read():
    if char not in string.punctuation:
        puncless += char
lowered = puncless.lower()
newLineless = lowered.replace("\n", " ")
splitted = newLineless.split(' ')
sortedList = sorted(splitted)

words = {}
wordLength = {}
for word in sortedList:
    if word in words:
        words[word] += 1
    else:
        words[word] = 1
        
for word in words:
    if len(word) >= 9:
        print(word, "\t", words.get(word))
    else:
        print(word, "\t", words.get(word))
keys = len(words)
print(keys)


##for word in words:
##    wordLength = []
##    wordLength += str(len(word))
##    maxLength = max(wordLength)
##    print(maxLength)

##address = []
##for line in puncless:
##    splitted = line.split()
##    address += splitted
##print(address)

