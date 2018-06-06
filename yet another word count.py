
gettysburg = open("C:/Users/Roger/Documents/GitHub/LaunchCode/gettysburg.txt", "r")

address = []
for line in gettysburg:
    splitted = line.split()
    address.append(splitted)

print(address)
