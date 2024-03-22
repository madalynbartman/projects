def brick_sort(a):
    n = len(a)
    is_sorted = False
    while not is_sorted:

        #go through even indexes
        for i in range(0, n-1, 2):
            yield a, [i], [], []
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                is_sorted = False

        # assume that is_sorted is True
        is_sorted = True

        # go through odd indexes
        for i in range(1, n-1, 2):
            yield a, [], [i], []
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]    
                is_sorted = False
