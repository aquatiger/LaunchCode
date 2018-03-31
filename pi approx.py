# compare various approximations of pi
import math
import random

# simplest estimate
a = 22/7
print(a)

# next simplest
b = 355/113
print(b)

# from wikipedia:
# In 1910, the Indian mathematician Srinivasa Ramanujan found several rapidly converging infinite series
c = (2*math.sqrt(2)/9801) * (((math.factorial(4*0))*(1103+26390*0)) / ((math.factorial(0)**4)*(396**(4*0))))
d = (2*math.sqrt(2)/9801) * (((math.factorial(4*1))*(1103+26390*1)) / ((math.factorial(1)**4)*(396**(4*1))))
e = (2*math.sqrt(2)/9801) * (((math.factorial(4*2))*(1103+26390*2)) / ((math.factorial(2)**4)*(396**(4*2))))
f = (2*math.sqrt(2)/9801) * (((math.factorial(4*3))*(1103+26390*3)) / ((math.factorial(3)**4)*(396**(4*3))))
g = (2*math.sqrt(2)/9801) * (((math.factorial(4*4))*(1103+26390*4)) / ((math.factorial(4)**4)*(396**(4*4))))
h = (2*math.sqrt(2)/9801) * (((math.factorial(4*5))*(1103+26390*5)) / ((math.factorial(5)**4)*(396**(4*5))))
i = (2*math.sqrt(2)/9801) * (((math.factorial(4*6))*(1103+26390*6)) / ((math.factorial(6)**4)*(396**(4*6))))
j = (2*math.sqrt(2)/9801) * (((math.factorial(4*7))*(1103+26390*7)) / ((math.factorial(7)**4)*(396**(4*7))))
k = (2*math.sqrt(2)/9801) * (((math.factorial(4*8))*(1103+26390*8)) / ((math.factorial(8)**4)*(396**(4*8))))
l = (2*math.sqrt(2)/9801) * (((math.factorial(4*9))*(1103+26390*9)) / ((math.factorial(9)**4)*(396**(4*9))))
m = c + d + e + f + g + h + i + j + k + l
print(1/m)

print(math.pi)

c = 0
for i in range(10):
    c +=  (2*math.sqrt(2)/9801) * (((math.factorial(4*i))*(1103+26390*i)) / ((math.factorial(i)**4)*(396**(4*i))))

print(1/c)
