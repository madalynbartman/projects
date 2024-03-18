import random

def binarySearch(li, element):
    li.sort()
    top = len(li)
    bottom = 0

    while top > bottom:
        print(len(li[bottom:top]))
        middle = (top + bottom)//2
        if element == li[middle]:
            return middle
        elif element < li[middle]:
            top = middle
        elif element > li[middle]:
            bottom = middle

    return -1
 
li = [int(1000*random.random()) for i in range(10000)]
print(binarySearch(li, li[random.randrange(0, len(li))]))