# copied most of this even though I could write it.
# I did write the random parts
import random
import turtle


def isInScreen(w, t):
    if random.random() > 0.1:
        return True
    else:
        return False


t = turtle.Turtle()
wn = turtle.Screen()

t.shape('turtle')
while isInScreen(wn, t):
    coin = random.randrange(0, 2)
    if coin == 0:              # heads
        t.left(random.randrange(180))
    else:                      # tails
        t.right(random.randrange(180))

    t.forward(50)

wn.exitonclick()
