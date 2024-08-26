# Prompt: Write a Python function that takes a list of integers and returns a new list containing only the even numbers from the original list.
# My submission

def my_funct(my_list):
    new_list = []
    for i in my_list:
        if i % 2 == 0:
            new_list.append(i)
    return new_list
