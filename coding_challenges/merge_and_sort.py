# Prompt: Write a Python function that takes two sorted lists of integers as input and returns a single sorted list that contains all the elements from both input lists.
# My submission

def my_func(list1, list2):
    my_list = list1 + list2
    return sorted(my_list)
