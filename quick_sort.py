import random

def quick_sort(data,low,high):

    if low<high:
        pivot = random.randint(low,high)
        data[low],data[high] = data[high],data[low]

        mid = partion(data,low,high)
        quick_sort(data,low,mid-1)
        quick_sort(data,mid+1,high)


def partion(data,low,high):
    i,j = low,low
    pivot = data[high]
    for j in range(low,high):
        if data[j] < pivot:
            data[i],data[j] = data[j],data[i]
            i += 1
    data[high],data[i] = data[i],data[high]
    return i

a = [random.randint(0,100) for x in range(10)]
quick_sort(a,0,len(a)-1)
print(a)