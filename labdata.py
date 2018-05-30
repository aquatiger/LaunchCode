# Interpret the data file labdata.txt such that each line contains a an x,y coordinate pair.

import turtle


wn = turtle.Screen()       # Set up the window and its attributes
wn.bgcolor("beige")
turtle.setworldcoordinates(-10, -10, 100, 100)
hadir = turtle.Turtle()     # create hadir
hadir.color('orange')
hadir.shape("circle")
hadir.speed(0)
datums = open("C:/Users/Roger/Documents/GitHub/LaunchCode/labdata.txt", "r")



def turtlePart():
    for aline in datums:
        splitted = aline.split()
        coords = [int(i) for i in splitted]
        x = coords[0]
        y = coords[1]
        xTotal = 0
        print(xTotal)
        yTotal = 0
        print(yTotal)
        for i in coords:
            hadir.penup()
            hadir.goto(x, y)       # move hadir to the starting position for the next coordinates
            hadir.pd()
            hadir.stamp()
            hadir.penup()            
            xTotal += coords[0]
            yTotal += coords[1]
            n = len(coords)
            print(splitted[0], min, max)
            print(splitted[1], min, max)
            print(n)
            xBar = xTotal / n
            yBar = yTotal / n
    datums.close()



def plotRegression():
    for aline in datums:
        splitted = aline.split()
        coords = [int(i) for i in splitted]
        x = coords[0]
        y = coords[1]
        xTotal +=  x
        yTotal += y


            


##        m = ((x * y) - (n * xBar * yBar)) / x ** 2 - (n * (x ** 2))
##        yLine = yBar + m * (i - xBar)

turtlePart()
#plotRegression()    
turtle.exitonclick()
