import math

def NumberOf1( n):
    # write code here
    if n >= 0:
        return bin(n).count('1')
    else:
        abs_n = abs(n)
        return 1 + (bin(2**int(math.log(abs_n,2)+1) - 1 - abs_n)).count(1)

print(NumberOf1(-8))