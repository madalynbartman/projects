# Prompt: Write a Python function that takes a list of integers and returns a new list containing only the odd numbers from the original list.
# My submission:

def my_funct(n):
    new_list = []
    for i in n:
        if i % 2 != 0:
            new_list.append(i)
    return new_list
