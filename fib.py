
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

fib(16)
##[fib(n) for n in range(16)]
##[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]