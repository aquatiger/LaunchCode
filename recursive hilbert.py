# draw a Hilbert curve

import turtle


def hilbert(t, n):
    if n < 8:
        t.forward(30)
        t.left(90)
        t.forward(30)
        t.left(90)
        t.forward(30)
        t.right(90)
        hilbert(t, n+1)









def main():
    hadir = turtle.Turtle()
    windo = turtle.Screen()
    hilbert(hadir, 3)
    windo.exitonclick()

main()


# hilbert equation = (2 ** n) - (1 /  (2 ** n))


##def fib(n):
##    if n < 2:
##        return n
##    return fib(n-1) + fib(n-2)
##
##print(fib(35))
