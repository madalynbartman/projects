print("Welcome to my computer quiz!")

playing = input("Do you want to play? (yes or no) ")

# takes the user's answer and makes it lowercase to ensure any ver of yes works
if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score +=1
else:
    print('Incorrect!')

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score +=1
else:
    print('Incorrect!')

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score +=1
else:
    print('Incorrect!')

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score +=1
else:
    print('Incorrect!')
    # add str() to score because score is an int and needs to be converted
    print("You got " + str(score) + " questions correct!")
    print("You got " + str(score / 4 * 100) + "%")
