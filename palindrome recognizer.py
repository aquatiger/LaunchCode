# function to recognize a palindrome

def  recognizer(text):
    replaced = text.replace(" ", "")
    lowered = replaced.lower()
    print(lowered)
    reverseText = lowered[::-1]
    print(reverseText)
    if lowered == reverseText:
        print(True)
    else:
        print(False)


recognizer("Acrobats stab orca")
