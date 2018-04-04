"""
Did most of this on my own, but when I got stuck and it didn't work, I did copy the
salient parts into my code from the website. However, despite what the instructor
says this code only works for odd-number-pointed stars. I tried 6, 8, and 10 which did
not work; and 5, 7, 9 and it does.
"""

import turtle
wn = turtle.Screen()


def nPoints(t, n):
    for i in range(n):
        t.forward(100)
        t.left(180 - 180/n)

hadir = turtle.Turtle()
hadir.speed(0)

nPoints(hadir, 10)

wn.exitonclick()
