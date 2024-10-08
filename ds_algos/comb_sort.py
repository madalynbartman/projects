def determine_next_gap(gap):
    next_gap = max(1, int(gap / 1.3))
    return next_gap


def comb_sort(a):
    gap = n = len(a)
    is_sorted = False
    while not is_sorted or gap != 1:

        # determine next gap
        gap = determine_next_gap(gap)

        # traverse the array
        is_sorted = True
        for i in range(0, n-gap):
            yield a, [i], [i+gap], []
            if a[i] > a[i+gap]:
                a[i], a[i+gap] = a[i+gap], a[i]
                is_sorted = False

a = [2, 5, 4, 1, 3]
# print(a)
# comb_sort(a)       
# print(a)         
