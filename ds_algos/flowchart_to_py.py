try:
    num = float(input("Enter a number: "))
    while num > 0:
        num = num -1
        print(num)
    print("Done")
except: 
    print("Not a valid number")
    