# Write a program called alice_words.py
# that creates a text file named alice_words.txt
# containing an alphabetical listing of all the words and
# the number of times each wrod occurs

import string

file_name = 'oxford.txt'

wordset = {}
with open(file_name, 'r') as f:
    for line in f:
        word_list = line.split(' ')
        print(word_list)
        for word in line:
            cleanWord = word.strip()
        print(cleanWord)
        sentence2 = word_list.lower()
        print(sentence2)
        
        

        for word in word_list:
            word_list[word] = word_list[word].strip(string.punctuation)
            print(word_list)

        if word_list[i] in wordset:
            wordset[word_list[i]] += 1
        else:
            wordset[word_list[i]] = 1
        print(wordset)
        
f.close()

##print(string.punctuation)
##def alice_words(file):
##    words = {}
##    with open(file, "r") as infile:
##        for line in infile:
##            lines = line.strip(string.punctuation)
##            print(line)
##            print(lines)
##            splitted = lines.split()
##            print(splitted)
##
##    # maybe look at the exercises at Code Guild
##    for word in line:
##        if word in words:
##            words[word] += 1
##        else:
##            words[word] = 1
##    print(words)
##    infile.close()
##
##alice_words("C:/Users/Roger/Documents/Roger/Python/statistics notebook.txt")
##





##def counter(text):
##    alphabet = {}
##    for achar in text:
##        if achar in alphabet:
##            alphabet[achar] += 1
##        else:
##            alphabet[achar] = 1
##        items = alphabet.items()
##        print(items)
##
##    keys = alphabet.keys()
##    print(keys)
##    for char in sorted(keys):
##        print(char, "\t", alphabet[char])
##
##counter(sentence)
