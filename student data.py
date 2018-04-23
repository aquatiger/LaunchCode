
innie = open("C:/Users/Roger/Documents/Roger/Python/studentdata.txt", 'r')


for aline in innie:
    items = aline.split()
    if len(items[1:]) > 6:
        print(items[:])

innie.close()
