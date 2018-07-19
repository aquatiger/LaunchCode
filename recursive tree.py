import turtle

def tree(branchLen, width, t):
    if branchLen > 5:
        t.pensize(width)
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15, width-5, t)
        t.left(40)
        tree(branchLen-15, width-5, t)
        #t.pencolor("yellow")        
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


"""
In order to understand recursion, I've listed the following code from:
http://interactivepython.org/runestone/static/thinkcspy/IntroRecursion/CalculatingtheSumofaListofNumbers.html

This code returns 25:
def listsum(numList):
   if len(numList) == 1:
        return numList[0]
   else:
        return numList[0] + listsum(numList[1:])

print(listsum([1,3,5,7,9]))
-----
This code returns 1:
def listsum(numList):
   if len(numList) >= 1:                greater than sign
        return numList[0]
   else:
        return numList[0] + listsum(numList[1:])

print(listsum([1,3,5,7,9]))
-----
This code returns  25:
def listsum(numList):
   if len(numList) == 1:
        return numList[0]
   else:
        return numList[0] + listsum(numList[1:])

print(listsum((1,3,5,7,9)))            a tuple instead of a list
-----
This code returns TypeError: object of type 'int' has no len() on line 2:
def listsum(numList):
   if len(numList) == 1:
        return numList[0]
   else:
        return numList[0] + listsum(numList[1:])

print(listsum((3)))                        a single integer instead of a list
-----
This code returns 3:
def listsum(numList):
   if len(numList) == 1:
        return numList[0]
   else:
        return numList[0] + listsum(numList[1:])

print(listsum([3]))                     a list of a single integer
-----
This code returns TypeError: listsum() takes exactly 1 arguments (2 given) on line 7
def listsum(numList):
   if len(numList) == 1:
        return numList[0]
   else:
        return numList[0] + listsum(numList[1:])

print(listsum((1,3,5),(7,9)))           two sets of tuples

"""
