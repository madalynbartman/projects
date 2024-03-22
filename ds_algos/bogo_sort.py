import random
from matplotlib import pyplot

def bogo_sort(a):
    n = len(a)
    is_sorted = False
    while not is_sorted:

        # swap two elements
        i = random.randint(0,n-1)
        j = random.randint(0,n-1)
        a[i], a[j] = a[j], a[i]
        yield a

        # check if sorted
        is_sorted = True
        for i in range(1,n):
            if a[i] < a[i-1]:
                is_sorted = False
                break

# sorting in place (no return statement)
# print(a)
# bogo_sort(a)
# print(a)
            
def visualize(sorting_algorithm, n):

    # create array
    a = random.sample(range(1,n+1), n)

    # generate sorting process
    sorting_process = sorting_algorithm(a)

    # visualize sorting process
    while True:

        next_a = next(sorting_process, None)

        if next_a is None:
            break

        else:
            # visualize
            pyplot.bar(x = range(1,len(a)+1), height = next_a)
            pyplot.axis("off")
            pyplot.pause(0.1)
            pyplot.clf()
    pyplot.show()

visualize(bogo_sort, n = 5)
