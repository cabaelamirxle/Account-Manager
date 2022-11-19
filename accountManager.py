master_pwd = input("What is the master password? ")

def view():
    with open('accounts.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    
    with open('accounts.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n")
        

while True:
    mode = input("Would you like to add a new password or view existing ones(add, view)?, press q to quit. ")
    if mode == "q":
        break
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid.")
        continue