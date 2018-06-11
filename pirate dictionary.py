"""
Pirate dictionary
Have user input sentence (done)
and have computer translate from English into Pirate

replace word with pirate.value()
need a string to add the word for completion

"""
import string

pirate = {'sir': "matey", 'hotel': 'fleabag inn',  'student': 'swabie', 'boy': 'matey', 'madam': 'proud beauty',
          'professor': 'foul blaggart', 'restaurant': 'galley', 'your': 'yer', 'excuse': 'arrrrr', 'students': 'swabbies',
          'are': 'be', 'lawyer': 'foul blaggart', 'the': "th'", 'restroom': 'head', 'my': 'me', 'hello': 'avast', 'is': 'be',
          'man': 'matey'}

sentence = input("Please enter a sentence in English to be translated into Pirate.")

for word in sentence:
    if word == pirate.keys():
        
        

##
##puncless = ""
##for char in sentence:
##    if char not in string.punctuation:
##        puncless += char
##lowered = puncless.lower()
##newLineless = lowered.replace("\n", " ")
##splitted = newLineless.split(' ')
##sortedList = sorted(splitted)
##
##words = {}

