# If..

# I wake up
# If I'm hungry 
#     I eat breakfast

# I leave my house
# if it's cloudy
#     I bring an umbrella
# otherwise
#     I bring sunglasses

# Im at a resturant
# if I want meat
#     I order a steak
# otherwise if I want pasta
#     I order spaghetti & meatballs
# otherwise
#     I order a salad

is_female = True
is_tall = True

if is_female and is_tall:
    print("You are a tall female")
elif is_female and not(is_tall):
    print("You are a short female")
elif not(is_female) and is_tall:
    print("You not a female but are tall")
else:
    print("You neither female nor tall")