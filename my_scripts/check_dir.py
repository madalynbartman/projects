import os

# Make a script that will list directories and find a specific one
# If dir we want is not there, make it

# Ask user for the name of the directory they want to find
print("Enter the name of the directory you'd like like to search for: ")
dir_name = str(input(""))

# Add a / to the fornt of it so it can be added either to their relative or absolute path
partial_path = "/" + dir_name

# Ask the user if they'd like to search relative to their current working directory or root
print("Would you like to initiate the search from your current working directory or root? (cwd or root)")
while True:
    if input("") == "root" or "/":
        dir_path = "." + partial_path
        break
    elif input() == "cwd" or "pwd":
        dir_path = os.getcwd() + partial_path
        break
    else:
        print("Invalid response! Please enter either cwd or root..")

# Search for the directory and report status back to user
if os.path.exists(dir_path) == True:
    print("Directory exists!")
    exit()
else:
    print("Directory not found! Would you like to create it? (y or n) ")

# Create the directory if it doesn't exists and the user opts in
# Otherwise, end the program
response = input("")
while True: 
    if response == "y":
        print("Alright! Would you like to create it in the current working directory or in a custom location? (cwd or custom)")
        response = input("")
        while True:
            if response == "cwd":
                print("Creating directory..")
                os.mkdir(dir_name)
                print("Done!")
                break
            elif response == "custom":
                print("Please enter the custom path (including the name of the directory to be created): ")
                custom_path = input("")
                print("Creating directory..")
                os.mkdir(custom_path)
                print("Done!")
                break
            else:
                print("Invalid response! Please enter cwd or custom..")
        break
    elif response == "n":
        print("Exiting..")
        break
    else:
        "Invalid response! Please enter y or n.. "
