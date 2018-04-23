

import turtle


def turtlePart():
    wn = turtle.Screen()       # Set up the window and its attributes
    wn.bgcolor("beige")
    setworldcoordinates(-10, -10, 100, 100)
    hadir = turtle.Turtle()     # create hadir
    hadir.color('orange')

    for i in range(1,6):
        sz =+ i*40
        drawSquare(hadir, sz)   # Call the function to draw the square
        hadir.penup()
        hadir.backward(20)       # move hadir to the starting position for the next square
        hadir.right(90)
        hadir.forward(20)
        hadir.left(90)
        hadir.pendown()




def plotRegression():
    
     datums = open("C:/Users/Roger/Documents/GitHub/LaunchCode/labdata.txt", "r")

     for aline in datums:
        splitted = aline.split()
        coords = [int(i) for i in splitted]
        x = splitted[0]
         y = splitted[1]
    xTotal = 0
    yTotal = 0
    for i in coords:
        xTotal += coords[0]
        yTotal += coords[1]
        n = len(coords)
        print(splitted[0], min, average, max)
    xBar = xTotal / n
    yBar = yTotal / n

    m = ((x * y) - (n * xBar * yBar)) / x ** 2 - (n * (x ** 2))
    yLine = yBar + m * (i - xBar)

turtlePart()
plotRegression()    
datums.close()
wn.exitonclick()
