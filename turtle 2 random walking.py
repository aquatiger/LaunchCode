# copied most of this even though I could write it.
# I did write the random parts

import random
import turtle


def isInScreen(w, t):
    if random.random() > 0.5:
        return True
    else:
        return False


t = turtle.Turtle()
t2 = turtle.Turtle()
t.shape('turtle')
t2.shape('triangle')

##t = turtle.setposition(random.randrange(-100, 100), random.randrange(-100, 100))
##t2 = turtle.setposition(random.randrange(-100, 100), random.randrange(-100, 100))

wn = turtle.Screen()


while isInScreen(wn, t):
    coin = random.randrange(0, 2)
    if coin == 0:              # heads
        t.left(random.randrange(180))
        t2.left(random.randrange(180))
    else:                      # tails
        t.right(random.randrange(180))
        t2.right(random.randrange(180))
    t.forward(50)
    t2.forward(50)
wn.exitonclick()
