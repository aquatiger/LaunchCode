import turtle              # 1.  import the modules
import random
wn = turtle.Screen()       # 2.  Create a screen
wn.bgcolor('darkgreen')

lance = turtle.Turtle()    # 3.  Create two turtles
andy = turtle.Turtle()
aquatiger = turtle.Turtle()
hadir = turtle.Turtle()
lance.color('red')
andy.color('blue')
lance.shape('turtle')
andy.shape('turtle')
aquatiger.color('aqua')
aquatiger.shape('turtle')
hadir.color('yellow')
hadir.shape('turtle')

andy.up()                  # 4.  Move the turtles to their starting point
lance.up()
aquatiger.up()
hadir.up()
andy.goto(-100,20)
lance.goto(-100,-20)
aquatiger.goto(-100, 60)
hadir.goto(-100,-60)
andyRandom = random.randint(0,10)
lanceRandom = random.randint(0,10)
aquatigerRandom = random.randint(0,10)
hadirRandom = random.randint(0,10)

# your code goes here
for i in range(45):
    andy.speed(andyRandom)
    andy.forward(andyRandom)
    andy.stamp()
    lance.speed(lanceRandom)
    lance.forward(lanceRandom)
    lance.stamp()
    aquatiger.speed(aquatigerRandom)
    aquatiger.forward(aquatigerRandom)
    aquatiger.stamp()
    hadir.speed(hadirRandom)
    hadir.forward(hadirRandom)
    hadir.stamp()

wn.exitonclick()
