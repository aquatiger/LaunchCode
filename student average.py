# calculates the average grade for each student,
# and print out the student’s name along with their average grade.

innie = open("C:/Users/Roger/Documents/Roger/Python/studentdata.txt", 'r')

for aline in innie:
    splitted = aline.split()
    scores = splitted[1:]
    scores = [int(i) for i in scores]
    print(scores)
    total = 0
    for i in scores:
        total += i
        average = total / (len(scores))
    print(splitted[0], average)

innie.close()
