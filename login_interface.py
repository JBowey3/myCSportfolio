#12/4
#james bowey
#login thing

#init

#func
def login():
    valid_username = "jamesb"   #set user variable
    valid_password = "ComputerScience1"   #set password variable
    user = input("Enter your username here: ")  #login prompt
    User = user.lower()
    passcode = input("Enter your password here: ")
    if user == valid_username and passcode == valid_password:
        print("Welcome in!")
    else:                            #result
        print("One or more of your username and password is incorrect, try again: ")

#main
login()
