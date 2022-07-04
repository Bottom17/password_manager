from cryptography.fernet import Fernet

# key + password + text to encrypt = random text
# random text + key + password = text to encrypt
"""" Function to write and save a key in a file
def write_key():
    key = Fernet.generate_key()
    with open( "key.key", "wb") as key_file:
        key_file.write(key)"""

# Function that will open the file that the function write_key created, read it
# and save it in the variable key, close it and return the value of the variable key
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

# With the master password we can encrypt 
# master_password = input("What is the master password? ")
# The encryption key is equal to the value returned by the function load_key 
# and the master password in bytes
key = load_key() # + master_password.encode()
fer = Fernet(key)

def view():
    with open("password.txt", "r") as file:
        for line in file.readlines():
            data = line.rstrip()
            name, psw = data.split("|")
            print("Username:", name, ", Password:", fer.decrypt(psw.encode()).decode())

def add():
    print("You can now add a new account")
    username = input("Type the username: ")
    password = input("Type the password: ")
    with open("password.txt", "a") as file:
        file.write(username + "|" + fer.encrypt(password.encode()).decode() + "\n")

while True:
    mode = input("Would you like to ADD a new password or VIEW existing ones or type Q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue