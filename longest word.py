
"""
Try to find the longest word in the text and
give the length of that word

"""


import string

gettysburg = open("C:/Users/Roger/Documents/GitHub/LaunchCode/gettysburg.txt", "r")

puncless = ""
for char in gettysburg.read():
    if char not in string.punctuation:
        puncless += char
newLineless = puncless.replace("\n", " ")
splitted = newLineless.split(' ')
print(puncless)

longest = {}
for word in splitted:
    longest[len(word)] = word
maximized = sorted(longest)
goal = longest.get(maximized[-1])

print('The longest word in the text is ' + '\"' + goal + '\"' + ' and it is', maximized[-1], 'characters long.')

gettysburg.close()
