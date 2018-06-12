"""
Pirate dictionary (done)
Have user input sentence (done)
and have computer translate from English into Pirate (done, for what this exercise is)
the input cannot include punctuation or capitalization

"""

pirate = {'sir': "matey", 'hotel': 'fleabag inn',  'student': 'swabie', 'boy': 'matey', 'madam': 'proud beauty',
          'professor': 'foul blaggart', 'restaurant': 'galley', 'your': 'yer', 'excuse': 'arrrrr', 'students': 'swabbies',
          'are': 'be', 'lawyer': 'foul blaggart', 'the': "th'", 'restroom': 'head', 'my': 'me', 'hello': 'avast', 'is': 'be',
          'man': 'matey'}


sentence = input("Please enter a sentence in English to be translated into Pirate." + "\n" + "Pirates don't use punctuation: ")

pirated = ""
splitted = sentence.split(" ")
for word in splitted:
    if word in pirate:
        pirated += pirate[word] + " "
    else:
        pirated += word + " "
print(pirated)
        

