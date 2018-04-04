import turtle
wn = turtle.Screen()
hadir = turtle.Turtle()
hadir.speed(0)

hadir.pu()
hadir.goto(-75, 0)
def star5points(t):
    t.pd()
    t.left(108)
    for i in range(5):
        t.forward(100)
        t.left(144)
    t.pu()
    t.forward(200)
    
for i in range(5):
    star5points(hadir)



wn.exitonclick()
