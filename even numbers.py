"""
Sum up all the even numbers in a list.

"""

xs = list(range(1, 100))
print(xs)

evenNum = 0
for i in xs:
    if  i % 2 == 0:
        evenNum += i

print(evenNum)


