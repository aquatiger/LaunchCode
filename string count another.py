# Write a program that allows the user to enter a string.
# It then prints a table of the letters of the alphabet in alphabetical order
# which occur in the string together with the number of times each letter occurs

sentence = input("Please enter a sentence: ")
sentence = sentence.lower()

def counter(text):
    alphabet = {}
    for achar in text:
        if achar in alphabet:
            alphabet[achar] += 1
        else:
            alphabet[achar] = 1
        items = alphabet.items()
        print(items)

    keys = alphabet.keys()
    print(keys)
    for char in sorted(keys):
        print(char, "\t", alphabet[char])

counter(sentence)
