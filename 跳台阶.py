def jumpFloor( number):
    # write code here
    if number == 1:
        return 1
    elif number == 2:
        return 2
    a, b = 1, 2
    for i in range(3, number + 1):
        a, b = b, a + b
    return b

print(jumpFloor(4))