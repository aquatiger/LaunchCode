# Interpret the data file labdata.txt such that each line contains an x,y coordinate pair.
# Then draw a line in a different color to give an estimate of the points.
# This file works like I want, except for the blue line goes off the window
# regardless of the size determined by setworldcoordinates

import turtle


wn = turtle.Screen()       # Set up the window and its attributes
wn.bgcolor("beige")
turtle.setworldcoordinates(-10, -10, 100, 100)
hadir = turtle.Turtle()     # create hadir

def turtlePart():    
    hadir.color('orange')
    hadir.shape("circle")
    hadir.speed(0)
    datums = open("C:/Users/Roger/Documents/GitHub/LaunchCode/labdata.txt", "r")

    for aline in datums:
        splitted = aline.split()
        coords = [int(i) for i in splitted]
        x = coords[0]
        y = coords[1]
        for i in coords:
            hadir.pu()
            hadir.goto(x, y)       # move hadir to the starting position for the next coordinates
            hadir.pd()
            hadir.stamp()
            hadir.penup()

    datums.close()

def drawLine():
    hadir.color('blue')
    hadir.pensize(2)
    hadir.speed(0)
    datums = open("C:/Users/Roger/Documents/GitHub/LaunchCode/labdata.txt", "r")

    xList = []
    yList = []
    for aline in datums:
        splitted = aline.split()
        xList.append(int(splitted[0]))
        yList.append(int(splitted[1]))
        xList.sort()
        yList.sort()
    for i in xList:
        n = len(xList)
        xTotal = 0
        yTotal = 0
        xBar = xTotal / n
        yBar = yTotal / n
        m = ((int(splitted[0]) * int(splitted[1])) - (n * xBar * yBar)) / int(splitted[0]) ** 2 - (n * (int(splitted[0]) ** 2))
        yLine = yBar + m * (i - xBar)

    hadir.pu()
    hadir.goto(xList[0], yList[0])
    hadir.pd()
    hadir.lt(m)
    hadir.fd(yLine)

    datums.close()

turtlePart()
drawLine()
turtle.exitonclick()    




