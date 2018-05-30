import string

file_name = 'oxford.txt'
with open(file_name, "r") as infile:
    for line in infile:
        lines = line.strip(string.punctuation)
        print(line)
        print(lines)
        splitted = lines.split()
        print(splitted)
