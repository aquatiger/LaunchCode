# create multiple polygons in various colors

import turtle
wn = turtle.Screen()
wn.bgcolor("darkgreen")
hadir = turtle.Turtle()
hadir.speed(8)

for i in range(3):
    hadir.color('white')
    hadir.forward(40)
    hadir.left(120)

for i in range(4):
    hadir.color('red')
    hadir.forward(40)
    hadir.left(90)
    
for i in range(6):
    hadir.color('blue')
    hadir.forward(40)
    hadir.left(60)

for i in range(8):
    hadir.color('yellow')
    hadir.forward(40)
    hadir.left(45)

for i in range(10):
    hadir.color('silver')
    hadir.forward(40)
    hadir.left(36)
    
for i in range(12):
    hadir.color('black')
    hadir.forward(40)
    hadir.left(30)
