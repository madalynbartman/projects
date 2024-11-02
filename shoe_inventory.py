from collections import Counter

# Input
n = int(input())  # Number of shoes
shoe_sizes = list(map(int, input().split()))  # List of shoe sizes
m = int(input())  # Number of customers

# Using Counter to count the number of each shoe size
shoe_count = Counter(shoe_sizes)

# Total earnings
earnings = 0

# Process each customer
for i in range(m):
    size, price = map(int, input().split())
    if shoe_count[size] > 0:
        earnings += price
        shoe_count[size] -= 1

print(earnings)