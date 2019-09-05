def Fibonacci(n):
    # write code here
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    while n != 0:
        a, b = b, a + b
        n -= 1
    return a

print(Fibonacci(3))