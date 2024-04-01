# Simple script/game to ask a user for a password to retrieve some nuclear launch codes 
# Give them three tries
# If they guess correctly, give them the codes
# If they fail quote unquote lock the system :P

print("Welome to Nuclear Launch Codes R Us. What is the password?")
response = input("")
i = 0
while i < 3:
    if response == "megaton":
        print("Correct! The launch codes are: 4266")
        break
    else:
        i += 1
        attempts_remaining = 3 - i
        if attempts_remaining > 1: 
            print("Incorrect! You have",attempts_remaining, "attempts remaining before system lockdown..")
        elif attempts_remaining == 1:
            print("Incorrect! You have",attempts_remaining, "attempt remaining before system lockdown..")
        else:
            print("Incorrect! System lock down imminent..")
            print("System locked! Get rekt noob >:P")
        if i < 3:
            print("Try again: ")
            response == input("")
        