import turtle

wn = turtle.Screen()
wn.bgcolor("lightyellow")

hadir = turtle.Turtle()
hadir.color("darkgreen")
hadir.speed(0)

def spiral():
    hadir.left(180)
    hadir.forward(100)
