import turtle

def tree(branchLen, width, t):
    if branchLen > 5:
        t.pensize(width)
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15, width-5, t)
        t.left(40)
        tree(branchLen-15, width-5, t)
        t.pencolor("yellow")        
        t.right(20)
        t.backward(branchLen)
        t.pencolor("green")

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.speed(0)
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(100, 30, t)
    myWin.exitonclick()

main()
