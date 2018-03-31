import turtle

background = input("What color would you like your background to be? ")
wn = turtle.Screen()
wn.bgcolor(background)        # set the window background color

pencilColor = input("And what color would you like your line drawn? ")
tess = turtle.Turtle()
tess.color(pencilColor)              # make tess blue
pencilSize = int(input("One final question, how wide would you like your pen? "))
tess.pensize(pencilSize)                 # set the width of her pen

tess.forward(50)
tess.left(120)
tess.forward(50)

wn.exitonclick()                # wait for a user click on the canvas
