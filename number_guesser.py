import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit(): 
    top_of_range = int(top_of_range) # if is digit, converts it to int

else: 
    print('Please type a number next time.')
    quit()

if top_of_range <= 0:
    print('Please type a number larger than 0 next time')
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess) # if is digit, converts it to int
    else: 
        print('Please type a number next time.')
        continue

    if user_guess == random_number:
        print("You got it!")
        break

    elif user_guess > random_number:
        print('You were above the number!')
    else:
        print("You were below the number!")

print("You got it in", guesses, "guesses")

# print(random.randrange(-1, 10)) # does not inclde 10 can also do (10) it will start from 0
# print(random.randint(-1, 10)) # does include 10
# 38:56

