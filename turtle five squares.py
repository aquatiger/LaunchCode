
import turtle

def drawSquare(t, sz):
    """Make turtle t draw a square of with side sz."""
    
    for i in range(4):
        t.forward(sz)
        t.left(90)
    sz += i*20
    
wn = turtle.Screen()       # Set up the window and its attributes
wn.bgcolor("lightgreen")

alex = turtle.Turtle()     # create alex
alex.color('hotpink')

for i in range(1,6):
    sz =+ i*40
    drawSquare(alex, sz)   # Call the function to draw the square
    alex.penup()
    alex.backward(20)       # move alex to the starting position for the next square
    alex.right(90)
    alex.forward(20)
    alex.left(90)
    alex.pendown()

wn.exitonclick()
