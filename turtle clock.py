import turtle
hadir = turtle.Turtle()
hadir.shape("turtle")

hadir.stamp()

for leg in range(12):
    hadir.pu()
    hadir.forward(100)
    hadir.pd()
    hadir.forward(10)
    hadir.pu()
    hadir.forward(20)
    hadir.stamp()
    hadir.ht()
    hadir.goto(0,0)
    hadir.right(30)

