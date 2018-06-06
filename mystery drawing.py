# Draw a picture based on the txt file mystery

# When UP go to the next line, read x,y coordinates, go to that point
# When DOWN go to the next line, read x,y coordinates, go to that point and continue until UP

import turtle


wn = turtle.Screen()       # Set up the window and its attributes
wn.bgcolor("beige")
hadir = turtle.Turtle()     # create hadir
hadir.color('orange')
hadir.speed(0)
datums = open("C:/Users/Roger/Documents/GitHub/LaunchCode/mystery.txt", "r")

for aline in datums:
    splitted = aline.split()
    try:
        coords = [int(i) for i in splitted]
        x = coords[0]
        y = coords[1]
        hadir.goto(x, y)
    except:
        if splitted[0] == "UP":
            hadir.pu()
        elif splitted[0] == "DOWN":
            hadir.pd()

turtle.exitonclick()    


