lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Sheldon", "Mac", "Mark", "Alex", "Christina"]

friends.extend(lucky_numbers) # combine two lists
friends.insert(1, "Riley")
# friends.remove("Riley")
friends.pop()
# friends.clear()
friends.append("Scout <3")

print(friends)
print(friends.index("Alex"))
print(friends.count("Scout <3"))
lucky_numbers.reverse()
print(lucky_numbers)
lucky_numbers.sort()
print(lucky_numbers)

friends2 = friends.copy()