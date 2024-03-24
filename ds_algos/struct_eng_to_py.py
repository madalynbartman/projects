import time

id_num = "12345"
id_tries = 0
# Don't try to copy structured english into code in an exact way
# Just implement the gist of it

while True:
    id_check = input("Enter ID: ")
    if id_check == id_num:
        print("Allowing access..")
        break
    elif id_tries >= 4: # it's zero based 0,1,2,3,4 = 5 tries
        print("You have failed 5 times")
        print("System freezing..")
        time.sleep(10)
        id_tries = 0
    else: 
        print("Incorrect ID, try again.")
        id_tries += 1
