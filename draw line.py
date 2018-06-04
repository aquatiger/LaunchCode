
import turtle

def drawLine():
    hadir.color('blue')
    hadir.pensize(3)
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
    print(xList)
    print(yList)

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


turtle.exitonclick()

