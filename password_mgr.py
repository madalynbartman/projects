from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|") # creates a list
            print("User:", user, "| Password:", 
                  fer.decrypt(passw.encode().decode()))
            # print(line.rstrip()) # rstrip will strip the \n from our line

def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f: # the with keyword will automatically close the password for you
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
        
while True:
    mode = input("Would you like to add a new password or view existing ones? (view, add) Press q to quit. ").lower()
    if mode == 'q':
        break
    elif mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print('Invalid mode.')
        continue

