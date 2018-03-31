
import math
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')
fred = turtle.Turtle()

fred.pu()
fred.goto(-200,0)
fred.seth(60)
fred.pd()

for angle in range(360):
    y = math.sin(math.radians(angle))
    fred.right(y)
    fred.forward(2)

wn.exitonclick()
