def InversePairs( data):
    # write code here
    if data == [] or len(data) == 1:
        return 0
    P = 0
    for i in range(len(data) - 1):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                P += 1
    return P

print(InversePairs([1,2,3,4,5,6,7,0]))