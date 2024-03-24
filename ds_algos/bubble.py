# Sorting is just putting things in order
# Bubble sort

#      0  1  2  3  4  5  6  7  8  9 
lst = [5, 6, 0, 1, 2, 4, 3, 9, 8, 7]

# finds the biggest number in the list and bubbles it up to the top

#      5, 0, 6
#            1, 6
#               2, 6
#                  4, 6
#                     3, 6
#                        6, 9
#                           8, 9
#                              7, 9


# how it'd be done with a loop
for j in range(0, 10):
    check_for_swap = False 
    for i in range(0, 9):
        if lst[i] > lst[i + 1]:
            swap = lst[i]
            lst[i] = lst[i + 1]
            lst[i + 1] = swap
            check_for_swap = True
    if check_for_swap == False:
        break
            
print(lst)
