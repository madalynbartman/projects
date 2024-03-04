name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? (left or right) ")

if answer == "left":
    answer = input("You come to a river. You can walk around it or swim accross. (walk or swim) ")

    if answer == "swim":
        print("You drown and lose the game.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water, and lost the game.")
    else: 
        print('Not a valid option. You lose.')

elif answer == "right":
    answer = input('You come to a bridge. It looks wobbly. Do you want to cross it? (yes or no) ')

    if answer == 'no':
        print('You lose the game because you are a weenie.')
    elif answer == 'yes':
        print("You find a stranger on the other side and they give you gold. You win!!")

else:
    print('Not a valid option. You lose.')

print("Thank you for playing the game", name)