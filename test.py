def is_uglynumer( number):
    while number % 2 == 0:
        number //= 2
    while number % 3 == 0:
        number //= 3
    while number % 5 == 0:
        number //= 5
    return number == 1

print(is_uglynumer(6))
print(is_uglynumer((14)))