import turtle

wn = turtle.Screen()
wn.bgcolor("lightyellow")

hadir = turtle.Turtle()
hadir.color("darkgreen")
hadir.speed(0)


def spiral():
    hadir.left(180)
    size = 2
    for i in range(100):
        hadir.forward(size + 1)
        hadir.right(90)
        size += 2

#for i in range(100):
#    spiral()

spiral()

wn.exitonclick()
